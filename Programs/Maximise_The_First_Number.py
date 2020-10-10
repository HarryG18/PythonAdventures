def max_possible(n1, n2):
    n1, n2 = list(str(n1)), sorted(str(n2))
    for i in range(len(n1)):
        if n2 and n1[i] < n2[-1]:
            n1[i] = n2.pop()
    return int(''.join(n1))

def max_possible2(n1, n2):
    n2 = sorted(str(n2))
    return int(''.join(i if i >= n2[-1] and n2 else n2.pop() for i in str(n1)))
    # return int(''.join(n2.pop() if n2 and n2[-1] > i else i for i in str(n1)))

print(max_possible(8732, 91255))
print(max_possible2(8732, 91255))