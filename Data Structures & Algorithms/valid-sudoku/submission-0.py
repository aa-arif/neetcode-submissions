class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row_tracker = defaultdict(set)
        col_tracker = defaultdict(set)
        box_tracker = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.': 
                    continue
                    
                elif (board[row][col] in row_tracker[row] or 
                    board[row][col] in col_tracker[col] or 
                    board[row][col] in box_tracker[(row // 3, col //3)] ):
                    return False

                row_tracker[row].add(board[row][col])
                col_tracker[col].add(board[row][col])
                box_tracker[(row//3, col//3)].add(board[row][col])
        return True


