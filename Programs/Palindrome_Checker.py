# regular_expressions
import re

s = "malayalam"
s = re.sub(r'[^\w\s],', '', s)
print(s == s[::-1])
