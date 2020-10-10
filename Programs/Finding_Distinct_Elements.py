inputString = [1, 9, 8, 8, 7, 6, 1, 6]
inputString2 = [5, 5, 2, 4, 4, 4, 9, 9, 9, 1]

# Method 1 - For Looping and list appending
Unique = []
for k in range(len(inputString)):
    #print(inputString[k], " is seen ", inputString.count(inputString[k]), 'times')
    if inputString.count(inputString[k]) == 1:
        Unique.append(inputString[k])
print("Method 1: Looping and Lists : ",Unique)

# Method 2 - Print Concatenation
print("Method 2: Print Concatenation : ",[inputString[i] for i in range(len(inputString)) if inputString.count(inputString[i]) == 1])

# Method 3 - Function Creation
def Distinct_Elements (inpString):
    return [inpString[i] for i in range(len(inpString)) if inpString.count(inpString[i]) == 1]

print("Function Input String 1: ", Distinct_Elements(inputString))
print("Function Input String 2: ", Distinct_Elements(inputString2))