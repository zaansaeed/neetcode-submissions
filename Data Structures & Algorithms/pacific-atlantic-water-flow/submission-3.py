class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nRows = len(heights)
        nCols = len(heights[0])


        def dfs(i, j, prev, seen):
            if not 0<=i<nRows or not 0<=j<nCols:
                return
            if heights[i][j] < prev:
                return 
            if (i,j) in seen:
                return
            seen.add((i,j))
            
            dfs(i+1, j, heights[i][j], seen)
            dfs(i-1, j, heights[i][j], seen)
            dfs(i, j+1, heights[i][j], seen)
            dfs(i, j-1, heights[i][j], seen)
        visited_pac = set()
        for idx in range(nRows):
            dfs(idx, 0, 0, visited_pac)
        for col in range(nCols):
            dfs(0, col, 0, visited_pac)
   
        visited_atl = set()
        for idx in range(nRows):
            dfs(idx, nCols-1, 0, visited_atl)
        for col in range(nCols):
            dfs(nRows-1, col, 0, visited_atl)

        return [[r,c] for r,c in visited_pac & visited_atl]
        
        
        




        
        
            




