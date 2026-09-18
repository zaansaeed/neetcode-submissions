class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nRows = len(heights)
        nCols = len(heights[0])
        matrix = [[0] * nCols for _ in range(nRows)]
        visited = set()

        def dfs(i, j, prev):
            if not 0<=i<nRows or not 0<=j<nCols:
                return

            if heights[i][j] < prev:
                return 
            if (i,j) in visited:
                return
            visited.add((i,j))
            matrix[i][j] += 1
            
            dfs(i+1, j, heights[i][j])
            dfs(i-1, j, heights[i][j])
            dfs(i, j+1, heights[i][j])
            dfs(i, j-1, heights[i][j])
        
        for idx in range(nRows):
            dfs(idx, 0, 0)
        for col in range(nCols):
            dfs(0, col, 0)
        visited = set()
        for idx in range(nRows):
            dfs(idx, nCols-1, 0)
        for col in range(nCols):
            dfs(nRows-1, col, 0)
        
        ans = []
        for i in range(nRows):
            for j in range(nCols):
                if matrix[i][j] == 2:
                    ans.append([i,j])
        return ans




        
        
            




