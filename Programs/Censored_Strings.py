def uncensor(txt, vowels):
    for char in txt:
        if txt[txt.index(char)] == "*":
            txt = txt.replace(char, vowels[0], 1)
            if len(vowels) > 0: vowels = vowels[1:]
    return txt


def uncensor2(txt, vowels):
    txt = txt.replace('*', '{}')
    return txt.format(*vowels)


uncensor3 = lambda t,v : t.replace('*','{}').format(*v)
print(uncensor3("Wh*r* d*d my v*w*ls g*?", "eeioeo"))


def uncensor4(s, V):
    return s.replace('*', '%s') % tuple(V)



print(uncensor4("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor2("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))