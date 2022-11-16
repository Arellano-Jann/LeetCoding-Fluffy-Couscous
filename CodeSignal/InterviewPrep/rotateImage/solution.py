def solution(a):
    length = len(a)
    def transpose(): # flip along a diagonal line from top left to bottom right
        for row in range(length):
            for col in range(row+1): # remember that this is O(n^2 / 2)
                a[row][col], a[col][row] = a[col][row], a[row][col] # swap function
    def reflect(): # reflect vertically
        for row in range(length):
            for col in range(length//2): # only need to go through half of the columns to flip
                a[row][col], a[row][-col-1] = a[row][-col-1], a[row][col]
    transpose()
    reflect()
    return a
