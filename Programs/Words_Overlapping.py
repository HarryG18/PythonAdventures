def overlap(s1, s2):
    for i in range(len(s1)):
        if s2.find(s1[i::]) == 0:
            return s1[:i] + s2
    return s1+s2


def overlap2(s1, s2):
    for i in range(len(s1)):
        if s2.startswith(s1[i:]):
            return s1[:i] + s2
    return s1 + s2


print(overlap("sweden", "denmark"))
print(overlap("joshua", "osha"))
print(overlap("diction", "dictionary"))