def parse_roman_numeral(num):
    romanval = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    total = 0
    for i in range(len(num)):
        if i > 0 and romanval[num[i]] > romanval[num[i-1]]:
            total += romanval[num[i]] - 2*romanval[num[i-1]]
        else:
            total += romanval[num[i]]
    return total

print(parse_roman_numeral(532))