from fractions import Fraction as fr

def simplify(txt):
    return str(fr(txt))

def simplify2(txt):
    a,b = map(int, txt.split('/'))
    if a%b ==0:
        return str(a//b)
    for i in range(min(a,b),1,-1):
        if a%i ==0 and b%i ==0:
            return '{}/{}'.format(a//i,b//i)
    return txt


print(simplify("1236/68"))
print(simplify2("1236/68"))