import functools as f
def is_prim_pyth_triple(lst):
    if sum([i**2 for i in lst if i != max(lst)]) == max(lst)**2:
        gcd = lambda a,b: a if b==0 else gcd(b,a%b)
        #print(f.reduce(lambda x,y: g(x,y), lst))
        return 1 >= f.reduce(lambda x,y: gcd(x,y), lst)
    return False

#Easier to Read No2

def GCD2(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def is_prim_pyth_triple2(lst):
    a, b, c = sorted(lst)   
    triple = a**2 + b**2 == c**2
    #GCD2 = lambda x,y: x if y==0 else GCD2(y,x%y)
    primitive = max(GCD2(a, b), GCD2(a, c), GCD2(b, c)) == 1
    return triple and primitive

print(is_prim_pyth_triple2([3,4,5]))