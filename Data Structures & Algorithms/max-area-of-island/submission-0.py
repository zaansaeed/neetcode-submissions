class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0 
        
        numRows = len(grid)
        numCols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i > numRows-1 or j < 0 or j > numCols-1 or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1,j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 0:
                    continue
                else:
                    size = dfs(i, j)
                    maxSize = max(size, maxSize)

        return maxSize


