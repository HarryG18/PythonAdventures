from functools import reduce
import operator as op

def additive_persistence(n):
    count = 0
    while n > 9:
        n = sum(int(i) for i in str(n))
        count+=1
    return count

def multiplicative_persistence(n):
    count = 0
    while n > 9:
        product = 1
        for i in str(n):
            product *= int(i)
        n = product
        count += 1
    return count

def additive_persistence2(n):
    count = 0
    while True:
        n = reduce(op.add,list(map(int, str(n))))
        count += 1
        if n < 9:
            return count

def multiplicative_persistence2(n):
    count = 0
    while True:
        n = reduce(op.mul,list(map(int, str(n))))
        count+=1
        if n < 9:
            return count


print(additive_persistence(123456))
print(multiplicative_persistence(77))

print(additive_persistence2(123456))
print(multiplicative_persistence2(77))