class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        numRow = len(grid)
        numCol = len(grid[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        t = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if 0<=nr<numRow and 0<=nc<numCol and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            t+=1
        
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 1:
                    return -1
                    
        return t-1 if t!=0 else 0
