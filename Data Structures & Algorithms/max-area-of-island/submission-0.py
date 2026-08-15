class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rl = len(grid)
        cl = len(grid[0])
        max_area = 0
        def recurr(r,c):
            nonlocal area
            if r<0 or c<0 or r>=rl or c>=cl or grid[r][c]==0:
                return 0
            grid [r][c] = 0
            area +=1
            recurr(r+1,c)
            recurr(r-1,c)
            recurr(r,c+1)
            recurr(r,c-1)

            return 
        for i in range(rl):
            for j in range(cl):
                area =0
                if grid[i][j] == 1:
                    recurr(i,j)
                max_area = max(area,max_area)
        return max_area
        