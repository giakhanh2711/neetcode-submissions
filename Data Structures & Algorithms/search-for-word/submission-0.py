class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        nrows, ncols = len(board), len(board[0])
        def dfs(i, x, y, visited):
            if (x < 0 or x >= nrows or y < 0 or y >= ncols) or board[x][y] != word[i]:
                return False
            
            visited.append([x, y])

            if i == len(word) - 1:
                return True
                
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if [new_x, new_y] not in visited:
                    if dfs(i + 1, new_x, new_y, visited):
                        visited.pop()
                        return True

            visited.pop()
            return False
        
        visited = []
        for i in range(nrows):
            for j in range(ncols):        
                if dfs(0, i, j, visited):
                    return True
        
        return False
