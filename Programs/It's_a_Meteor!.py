def will_hit(equation, position):
    #print(equation.replace('=','==').replace('x','*{}'.format(position[0])).replace('y', str(position[1])))
    return eval(equation.replace('=','==').replace('x','*{}'.format(position[0])).replace('y', str(position[1])))



print(will_hit("y = -2x - 5", (0, 3)))