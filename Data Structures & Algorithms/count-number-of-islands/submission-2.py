class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        nrows = len(grid)
        ncols = len(grid[0])
        def dfs(x, y):
            grid[x][y] = "0"
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < nrows and 0 <= new_y < ncols and grid[new_x][new_y] == "1":
                    dfs(new_x, new_y)
        
        n_islands = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    n_islands += 1
                    dfs(i, j)
        
        return n_islands
