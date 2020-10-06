def who_won1(board):
    for x in range(len(board)):

        #Horizontal
        if len(set(board[x]))==1:
            return board[x][0]
        #Verticals
        if len(set([board[0][x],board[1][x],board[2][x]]))==1:
            return board[0][x]

        #Diagonals
    if len(set([row[i] for i,row in enumerate(board)])) ==1:
        return board[0][0]

    if len(set([row[2-i] for i,row in enumerate(board)])) ==1:
        return board[2][0]


#ATTEMPT 2

def who_won2(board):
    #Horizontal
    for x in board:
        if len(set(x))==1:
            return set(x).pop()
    #Verticals    
    for y in zip(*board):
        if len(set(y))==1:
            return set(y).pop()

    #Diagonals
    if len(set([row[i] for i,row in enumerate(board)])) ==1:
        return board[0][0]

    if len(set([row[2-i] for i,row in enumerate(board)])) ==1:
        return board[2][0]


#ATTEMPT 3

def who_won3(board):
    rows = board[:]
    columns = [list(i) for i in zip(*board)]
    diag1 = [set(board[i][i] for i in range(3))]
    print(diag1)
    diag2 = [set(board[i][2-i] for i in range(3))]
    for i in rows + columns + diag1 + diag2:
        if set(i) == {"X"}:
            return "X"
    return "O"


# a = board
who_won4 = lambda a: next(x for x in "XO" if [x, x, x] in a or (x, x, x) in zip(*a) or a[0][0] == a[1][1] == a[2][2] == x or a[0][2] == a[1][1] == a[2][0] == x)


print(who_won4([
	["O", "O", "X"],
	["X", "O", "O"],
	["X", "X", "O"],
]))   
