import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        fresh =0
        mi = 0
        rl = len(grid)
        cl= len(grid[0])
        q =collections.deque()
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        directions =[(-1,0),(1,0),(0,-1),(0,1)]
        while q and fresh >0:
            snap = len(q)
            for i in range(snap):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if nr <0 or nr >=rl or nc <0 or nc >=cl or grid[nr][nc] !=1:
                        continue

                    grid[nr][nc] = 2
                    fresh -=1
                    q.append((nr,nc))
            mi +=1
        if fresh > 0:
            return -1
        return mi




        