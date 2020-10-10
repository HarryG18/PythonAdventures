def freed_prisoners(prison):
    count = 0
    for i in prison:
        if i == (count+1)%2:
            count+=1
    return count * prison[0]


def freed_prisoners2(prison):
    return sum([1 if prison[i] != prison[i-1] else 0 for i in range(1, len(prison))]) + 1 if prison[0] == 1 else 0

print(freed_prisoners([1, 1, 1, 0, 0, 0]))
print(freed_prisoners2([1, 0, 1, 0, 1, 0]))
