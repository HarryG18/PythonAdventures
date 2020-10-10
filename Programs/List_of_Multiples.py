# Method 1 - Defining a method
def list_of_multiples (num,length):
    return [(i+1)*num for i in range(length)]

print(list_of_multiples(7,5))

# Method 2 - print list
num2,length2 = 7,5
print([(i+1)*num2 for i in range(length2)])