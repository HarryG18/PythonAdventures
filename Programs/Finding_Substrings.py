# 1 List Manipulation
string,substring = ('ABCDCDC'.strip(), 'CDC'.strip())
print("Method 1: Num of Instances : ", len([i for i in range(len(string)) if string[i:i+len(substring)] == substring]))


# 2 Regular Expressions
import re
a,b = ('ABCDCDC'.strip(),'CDC'.strip())
print("Method 2: Num of Instances : ", len(re.findall('(?='+b+')',a)))
