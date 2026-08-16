class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rl = len(grid)
        cl = len(grid[0])
        count = 0
        def recurr(r,c):
            if r<0 or c<0 or r>=rl or c>=cl or grid[r][c]=='0':
                return 
            grid [r][c] = '0'
            recurr(r+1,c)
            recurr(r-1,c)
            recurr(r,c+1)
            recurr(r,c-1)

            return 
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == '1':
                    count += 1 
                    recurr(i,j)
        return count
