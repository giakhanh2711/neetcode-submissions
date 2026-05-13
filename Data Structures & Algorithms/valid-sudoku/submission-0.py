class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_sets = [set() for _ in range(n)]
        col_sets = [set() for _ in range(n)]
        box_sets = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(n):
            for j in range(n):
                r_box, c_box = i // 3, j // 3

                if board[i][j] in box_sets[r_box][c_box]:
                    return False

                if board[i][j] in row_sets[i] or board[j][i] in col_sets[i]:
                    return False
                
                if board[i][j] != '.':
                    row_sets[i].add(board[i][j])
                    box_sets[r_box][c_box].add(board[i][j])
                    
                if board[j][i] != '.':
                    col_sets[i].add(board[j][i])

        return True