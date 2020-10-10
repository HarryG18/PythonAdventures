def advanced_sort(lst):
    return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]

def advanced_sort2(lst):
    sublst = []
    for element in lst:
        s = [i for i in lst if i == element]
        if s not in sublst:
            sublst.append(s)
    return sublst

print(advanced_sort([5, 4, 5, 5, 4, 3]))

print(advanced_sort2([5, 4, 5, 5, 4, 3]))