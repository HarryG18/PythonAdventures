def rearranged_difference(num):
    return int(''.join(sorted(str(num), reverse=True))) - int(''.join(sorted(str(num))))

def rearranged_difference2(num):
    n = ''.join(sorted(str(num)))
    return int(n[::-1])-int(n)



print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))

print(rearranged_difference2(972882))
print(rearranged_difference2(3320707))
print(rearranged_difference2(90010))