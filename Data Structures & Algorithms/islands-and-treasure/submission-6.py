class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []
        rl = len(grid)
        cl = len(grid[0])
        INF = 2147483647
        q = collections.deque()
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 0:
                    q.append((i,j))
        direction = [(-1,0),(1, 0),(0,-1), (0,1)]
        while q:
            r,c = q.popleft()
            for dr,dc in direction:
                nr = r + dr
                nc = c +dc
                if nr <0 or nr >=rl or nc <0 or nc >=cl or grid[nr][nc] !=INF:
                    continue
                grid[nr][nc] = grid[r][c]+1
                q.append((nr,nc))
        

        
  

        
        

        