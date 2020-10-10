# A number is Economical if the quantity of digits of its prime factorization
# (including exponents greater than 1) is equal to or lower than the digit quantity of the number itself.
# Given an integer n, implement a function that returns a string:
#
# "Equidigital" if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of n;
# "Frugal" if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of n;
# "Wasteful" if none of the two above conditions is true.

def is_economical(n):
    size = len(str(n))
    factors = []
    for i in range(2, int(n**0.5)+1, 1):
        while n == i:
            factors.append(i)
            n /= i
    if n>2: factors.append(int(n))
    nf =  [[str(i), factors.count(i)] for i in sorted(set(factors))]
    numofdig = sum(len(str(nf[i][1])) + len(nf[i][0]) if nf[i][1] > 1 else len(nf[i][0])  for i in range(len(nf)))

    return 'Equidigital' if numofdig == size else 'Frugal' if numofdig<size else 'Wasteful'



def is_economical2(n):
    x,y,i=len(str(n)),0,2
    while n!=1:
        c=0
        while not n%i:c+=1;n//=i
        if c:y+=(len((str(i))+(str(c) if c>1 else '')))
        i+=1
    return 'Equidigital' if x==y else 'Frugal' if x>y else 'Wasteful'



def is_economical3(n):
    size = len(str(n))
    i, y = 2, 0
    while n != 1:
        count=0
        while not n%i:
            count+=1;n//=i
        if count: y+=len((str(i))+(str(count) if count>1 else ''))
        i+=1
    return 'Equidigital' if size == y else 'Frugal' if y < size else 'Wasteful'



print(is_economical(452687))
print(is_economical2(452687))
print(is_economical3(452687))

