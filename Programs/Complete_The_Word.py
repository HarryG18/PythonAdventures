import re
def can_complete(initial, word):
    return bool(re.search(r'.*'.join(initial), word))

can_complete2 = lambda search, word: bool(re.search(r'.*'.join(search), word))

print(can_complete("eutl", "beautiful"))
print(can_complete2("eutl", "beautiful"))