def split(txt):
    count, s, out = 0, "", []
    for i in txt:
        s += i
        if i == '(': count+=1
        else : count -=1
        if count == 0:
            out.append(s)
            s = ""
    return out

def split2(txt):
    out, s = [], ""
    for i in txt:
        s+=i
        if s.count("(") == s.count(")"):
            out.append(s)
            s = ""
    return out

def split3(txt):
	i, grp = 0, []
	for j in range (1, len(txt)+1):
		if txt[i:j].count("(")==txt[i:j].count(")"):
			grp.append(txt[i:j])
			i = j
	return grp


print(split("()()()"))
print(split2("((()))(())()()(()())"))
print(split3("((()))(())()()(()())"))
