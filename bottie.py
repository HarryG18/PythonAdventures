import os
import sys
import requests
import time
import pytz
import redis
import json
import threading

from dotenv import load_dotenv
from binance.client import Client
from datetime import datetime

try:
    ProgramPath, api_key, api_secret, LeverageAmount, BotName, DebugMode, SwapTrades = sys.argv # pylint: disable=unbalanced-tuple-unpacking
    Debug = False if DebugMode == "false" else True
except Exception as e:
    print("Failed arg input, defaulting to env file")
    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    LeverageAmount = os.getenv('LEVERAGE')
    BotName = os.getenv('BOTNAME')
    Debug = os.getenv('DEBUG')
    SwapTrades = os.getenv('SWAP_TRADES')
    #Debug = True


    #   Dashboard
url = '188.166.75.218'
redis_port = 6379
redis_pass = 'VJJO5o1T!Ufd6UPtp^NX0IJOaV2e3!j9!z@!i7dqVpj3Fu1&WuBC8IDPmenD^yn$'
r = redis.Redis(host=url, port=redis_port, db=0, password=redis_pass)

    # Create Client and vars
client = Client(api_key, api_secret)
client.futures_change_leverage(symbol = 'BTCUSDT', leverage = LeverageAmount)

CurrentSignal = ""
TradeID = None  # in order gen
TradeSize = None  # in BTC
TradeBTCPrice = None  # in USDT
TradeStartTime = None  # in GMT
TradeProfit = 0  # in %
TradeCall = None  # long/short
TradeStatus = False  # active/inactive

prevTradeCall = None
prevType = None

def MakeTrade(TradeType):
    global TradeStatus
    global prevTradeCall
    global prevType
    global TradeID
    global TradeBTCPrice
    global TradeCall
    global TradeStartTime
    global TradeSize

    #print("Entered with trade type requested: " + TradeType)

    # define trade call: Sell if short, Buy if long
    side = "SELL" if TradeType == "short" else "BUY"
    # if not in trade already, make trade and store trade type and trade call either BUY or SELL
    if not TradeStatus:
        #print("Thinks not in trade")
        # calculate numbers
        balance = float(client.futures_account_balance()[0]['balance'])
        price = float(client.futures_mark_price(symbol="BTCUSDT")['markPrice'])
        TradeSize = round(((1.0 / price) * (balance * .9)
                           * float(LeverageAmount)), 3)

        try:
            
            if not Debug:
                #print("Hi")
                newtrade = client.futures_create_order(symbol="BTCUSDT", side=side, type="MARKET", quantity=TradeSize)
                recordTrade(newtrade)
                #print("test")
                #print(newtrade)
            else:
                
                newtrade = {'orderId' : "TestTrade"}
        except Exception as e:
            #print(e)
            return r.publish('Log', f"{BotName} - {BotName} failed to make trade due to {e}")

    # if in trade already, first do opposite order to get back balance, then order in direction of signal
    else:
        #print("Thinks in trade")
        # covers in case trading view sends multiple signals of the same (multiple longs or multuple shorts)
        #if side == prevTradeCall:
        #    return r.publish('Log', f"{BotName} Recieved the same signal from trading view as current trade")

        # if last order was a buy, then sell. vice versa

        try:
            if not Debug:
                #print("Hi")
                trade = client.futures_create_order(
                    symbol="BTCUSDT", side=side, type="MARKET", quantity=TradeSize)
                recordTrade(trade)
                #print("shouldve closed trade")

        except Exception as e:
            #print(e)
            return r.publish('Log', f"{BotName} - {BotName} failed to make trade due to {e}")
        else:
            # confirm prev trade no longer active
            #print(f"Trade Type: {prevType} is no longer active")

            #print("trying to make new trade")
            r.publish('Log', f"{BotName} - {BotName} closed current position with tradeID = {TradeID}")
            if SwapTrades:
              # calculate new numbers
              balance = float(client.futures_account_balance()[0]['balance'])
              price = float(client.futures_mark_price(
                  symbol="BTCUSDT")['markPrice'])
              TradeSize = round(((1.0 / price) * (balance * .9)
                                * float(LeverageAmount)), 3)

              try:
                  if not Debug:
                      #print("trying to order")
                      newtrade = client.futures_create_order(
                          symbol="BTCUSDT", side=side, type="MARKET", quantity=TradeSize)
                      recordTrade(newtrade)
                  else:
                      newtrade = {'orderId' : "TestTrade"}
              except Exception as e:
                  #print(e)
                  return r.publish('Log', f"{BotName} - {BotName} failed to make trade due to {e}")

    # define current trade for future trades
    prevTradeCall = side
    prevType = TradeType

    # if program reaches here, an order has been made
    #print("ordered: " + TradeType)
    TradeID = newtrade['orderId']
    TradeSize = TradeSize
    TradeBTCPrice = price
    TradeCall = TradeType
    TradeStartTime = datetime.now(pytz.timezone(
        'Europe/London')).strftime("%d:%m:%Y %H:%M:%S") + " GMT"
    TradeStatus = True
    Relay = {"BotName": BotName, "trade_pnl": TradeProfit, "trade_status": TradeStatus, "trade_id": TradeID, "trade_start_time": TradeStartTime, "trade_call": TradeCall, "trade_btc_price": TradeBTCPrice, "trade_size": TradeSize}
    r.set(BotName, str(Relay))
    return r.publish('Log', f"{BotName} - {BotName} made order with trade type: {TradeType}, with tradeID: {TradeID}")

def recordTrade(trade):
    orderId = trade['orderId']
    positionSide = trade['positionSide']
    origQty = trade['origQty']
    avgPrice = trade['avgPrice']
    print('logging trade')
    trade = {'orderId':orderId, 'positionSide':positionSide, 'origQty':origQty, 'avgPrice':avgPrice, 'BotName':BotName} 
    r.publish("NewTrade", json.dumps(trade))

def NewTrade(message):
    global CurrentSignal
    SignalName = message['data'].decode('utf-8')
    if SignalName == "long" or  SignalName == "short":
        if CurrentSignal != SignalName:
            MakeTrade(SignalName)
            CurrentSignal = SignalName
        #time.sleep(300)
        #print("Got Signal " + SignalName)
    else:
        r.publish('Log', f"{BotName} - This '{SignalName}' was sent in signal, {BotName} didn't know what to do with it")

def GetBotInfo(message):
    global LeverageAmount
    global TradeBTCPrice
    global TradeStatus
    global TradeCall
    if message == BotName:
        while True:
            if TradeStatus:
                # get pnl as %
                TradeProfit = calcPNL(TradeBTCPrice) * 100.0 * float(LeverageAmount)
                ##### Adding TP SL - check
                call = "SELL" if TradeCall == "long" else "BUY"
                if TradeProfit <= -30:
                    TradeStatus = False
                    client.futures_create_order(symbol="BTCUSDT", side=call, type="MARKET", quantity=TradeSize)
                    r.publish("Log", f"{BotName} - AutoClosed Trade due to SL hit")

                    Relay = {"BotName": BotName, "trade_pnl": 0.0, "trade_status": TradeStatus, "trade_id": TradeID,
                            "trade_start_time": TradeStartTime, "trade_call": TradeCall, "trade_btc_price": TradeBTCPrice, "trade_size": TradeSize}
                #elif TradeProfit >= 5:
                #    TradeStatus = False
                #    client.futures_create_order(symbol="BTCUSDT", side=call, type="MARKET", quantity=TradeSize)
                #    r.publish("Log", f"{BotName} - AutoClosed Trade due to TP hit")

                #    Relay = {"BotName": BotName, "trade_pnl": 0.0, "trade_status": TradeStatus, "trade_id": TradeID,
                #            "trade_start_time": TradeStartTime, "trade_call": TradeCall, "trade_btc_price": TradeBTCPrice, "trade_size": TradeSize}

                #####
                else:    
                    Relay = {"BotName": BotName, "trade_pnl": TradeProfit, "trade_status": TradeStatus, "trade_id": TradeID,
                            "trade_start_time": TradeStartTime, "trade_call": TradeCall, "trade_btc_price": TradeBTCPrice, "trade_size": TradeSize}
                r.publish("Status", json.dumps(Relay))
            else:
                r.publish("Log", f"{BotName} - Getting Info But No Active Trade")
            time.sleep(1)

def calcPNL(tradeprice):
    CurrentBTCPrice = float(client.futures_mark_price(
        symbol="BTCUSDT")['markPrice'])
    # check if signal was short or long
    diff = (CurrentBTCPrice - tradeprice)/tradeprice
    if (diff >= 0 and TradeCall == "long"):
        return diff
    elif (diff >= 0 and TradeCall == "short"):
        return -diff
    elif (diff <= 0 and TradeCall == "long"):
        return diff
    else:
        return -diff

    # get reqs for bot

#StatusThread = stat_red.run_in_thread(sleep_time=0.5)
response = r.get(BotName)
#print("Trade status before get info from redis: " + str(TradeStatus))
if response:
    activity = eval(response.decode('utf-8'))
    if activity:
        TradeStatus = activity['trade_status']
        #print("trade status after from redis: " + str(TradeStatus))
        TradeID = activity['trade_id']
        TradeSize = activity['trade_size']
        TradeBTCPrice = activity['trade_btc_price']
        TradeCall = activity['trade_call']
        TradeStartTime = activity['trade_start_time']
        TradeProfit = activity['trade_pnl']

#print(f"Thinks current trade size: {TradeSize}")
sig_red = r.pubsub(ignore_subscribe_messages=True)
sig_red.subscribe(**{'Signal': NewTrade})
SignalThread = sig_red.run_in_thread(sleep_time=0.5)

x = threading.Thread(target = GetBotInfo, args = (BotName,))
x.start()

