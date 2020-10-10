from string import ascii_letters as alpha

def atbash(txt):
    output = ""
    for a in txt:
        if a.isalpha():
            if a.isupper():
                if ord(a) > 77: output += chr(ord(a)-int(2*(ord(a)-77.5)))
                else: output += chr(ord(a)+int(2*(77.5-ord(a))))
            else:
                if ord(a) > 109: output += chr(ord(a)-int(2*(ord(a)-109.5)))
                else: output += chr(ord(a)+int(2*(109.5-ord(a))))
        else: output += a
    return output

def atbash2(txt):
    output = ""
    for a in txt:
        if a.isalpha():
            if a.isupper():
                n = 155;
            else:
                n = 219
            output += chr(n-ord(a))
        else:
            output += a
    return output

def atbash3(txt):
    return txt.translate(str.maketrans(alpha, alpha[::-1].swapcase()))


print(atbash("ApPle"))
print(atbash2("Christmas is the 25th of December"))
print(atbash3("Christmas is the 25th of December"))


# 65 77.5 90
# 97 109.5 122