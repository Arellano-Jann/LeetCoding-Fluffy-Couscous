# https://leetcode.com/problems/rotting-oranges/description/
def orangesRotting(grid: List[List[int]]) -> int:
    infectious = [] # implemented as a deque in python
    time = good = 0
    # count good and bad oranges
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            element = grid[r][c]
            if element == 0: continue
            if element == 1: good += 1 # count good oranges
            if element == 2: infectious.append((r,c)) # count infectious oranges and add to queue for BFS


    range_of_infection = [(0,1), (0,-1), (1,0), (-1,0)] # NSWE
    while infectious and good > 0: # while there are still infectious oranges and things to be infected
        for i in range(len(infectious)): # leverage ranged for loop
            row, col = infectious.pop(0) # pop the first element because if u pop in middle, things get weird bc u r modifying the queue while iterating through it
            for r, c in range_of_infection: # infects all the cardinal directions
                shifted_row = row + r
                shifted_col = col + c
                # print('here', good, row,r, col,c)
                if (0 <= (shifted_row) < ROWS and 0 <= (shifted_col) < COLS and grid[shifted_row][shifted_col] == 1):
                    # print(good, shifted_row, shifted_col)
                    good -= 1 # ORANGE INFECTED
                    infectious.append((shifted_row, shifted_col)) # ORANGE GOING TO INFECT U
                    grid[shifted_row][shifted_col] = 2 # ORANGE TRULY INFECT AAAAAA
        time += 1 # iterates time for each set of evil infectious oranges. this is not inside the leveraged for loop because that iterates through the oranges and we would essentially be counting how many infectious oranges there are
    return time if good == 0 else -1