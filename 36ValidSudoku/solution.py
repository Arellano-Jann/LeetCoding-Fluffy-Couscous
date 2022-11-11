def isValidSudoku(self, board: List[List[str]]) -> bool:
    # rows and column checker
    all_rows = collections.defaultdict(set)
    all_cols = collections.defaultdict(set)
    all_squares = collections.defaultdict(set)
    for row in range(9):
        for col in range(9):
            current_box = board[row][col]
            if current_box == '.':
                continue
            if current_box in all_rows[row]:
                return False
            if current_box in all_cols[col]:
                return False
            if current_box in all_squares[(row // 3, col // 3)]:
                return False
            
            all_rows[row].add(current_box)
            all_cols[col].add(current_box)
            all_squares[(row // 3, col //3)].add(current_box)
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))