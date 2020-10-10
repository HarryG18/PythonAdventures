def pentagonal(num):
    return sum(5*(i+1) for i in range(num-1))+1

###
#total = 1
#for i in range(number):
#    total += 5(number-1)
#print(total)
###


print(pentagonal(1))
print(pentagonal(2))
print(pentagonal(3))
print(pentagonal(8))

#1 6 16 31
#1 2 3  4
#num + 5(num-1)

