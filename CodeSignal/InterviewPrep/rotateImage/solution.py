def solution(a):
    length = len(a)
    def transpose():
        for row in range(length):
            for col in range(row+1):
                a[row][col], a[col][row] = a[col][row], a[row][col]
    def reflect():
        for row in range(length):
            for col in range(length//2):
                a[row][col], a[row][-col-1] = a[row][-col-1], a[row][col]
    transpose()
    reflect()
    return a
