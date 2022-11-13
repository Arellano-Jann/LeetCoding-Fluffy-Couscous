def problem1(numbers, left, right):
    res = []
    for i in range(len(numbers)):
        j = i + 1
        element = numbers[i]
        if element % (j) != 0:
            res.append(False) # maybe [True]
            continue
        for x in range(left,right+1):
            result = x * j
            if element == result:
                res.append(True)
                break
        if len(res) <= i: # if True wasn't appended
            res.append(False)
        
    return res

def problem2(s, t):
    res = 0
    s_digits = [x for x in s if x.isdigit()]
    t_digits = [x for x in t if x.isdigit()]
    for x in s_digits:
        index = s.index(x)
        current_s = s[:index] + s[index+1:]
        if current_s < t:
            res += 1
    for x in t_digits:
        index = t.index(x)
        current_t = t[:index] + t[index+1:]
        if current_t > s:
            res += 1
    return res


def problem3(field, x, y):
    ROWS = len(field)
    COLS = len(field[0])
    newField = []
    def checkAdjacent(row, col): # returns the num of mines near
        res = 0
        def check(a, b): # automates
            if field[a][b]:
                res += 1
                
        #right
        if col+1 < COLS:
            check(row, col+1)
        #left
        if col-1 >= 0:
            check(row, col-1)
        #down
        if row+1 < ROWS:
            check(row+1, col)
            #botright
            if col+1 < COLS:
                check(row+1, col+1)
            #botleft
            if col-1 >= 0:
                check(row+1, col-1)
        #up
        if row-1 >= 0:
            check(row-1, col)
            #topright
            if col+1 < COLS:
                check(row-1, col+1)
            #topleft
            if col-1 >= 0:
                check(row-1, col-1)
        return res
        
        
    def fill_when_zero(row, col): # modified newField to fill adjacent boxes
        pass
        
    for r in range(ROWS):
        current_row = []
        for c in range(COLS):
            field[r][c] = checkAdjacent(r, c)
            if field[r][c] == 0:
                fill_when_zero(r, c)
        newField.append(current_row)
    return newField