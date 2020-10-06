def can_see_stage(seats):
    columns = [list(i) for i in zip(*seats)]
    return all(sum([col[k+1]-col[k]>0 for k in range(len(col)-1)]) ==  len(col)-1 for col in columns)

def can_see_stage2(seats):
    columns = [list(i) for i in zip(*seats)]
    return all(all([c[k+1]-c[k]>0 for k in range(len(c)-1)]) for c in columns)

def can_see_stage3(seats):
	return all(sorted(set(row)) == list(row) for row in zip(*seats))

def can_see_stage4(seats):
  return all(all(x < y for x, y in zip(s, s[1:])) for s in zip(*seats))

print(can_see_stage(
    [[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]]))
