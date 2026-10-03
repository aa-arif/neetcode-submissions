class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9): 
            for col in range(9):
                curr = board[row][col]

                if curr == '.': 
                    continue

                if (curr in rows[row] or 
                    curr in cols[col] or 
                    curr in boxes[(row // 3, col // 3)]): 
                    return False

                rows[row].add(curr)
                cols[col].add(curr)
                boxes[(row // 3, col // 3)].add(curr)
                
        return True
