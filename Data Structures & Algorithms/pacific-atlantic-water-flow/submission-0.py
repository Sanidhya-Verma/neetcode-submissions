class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rl = len(heights)
        cl = len(heights[0])
        pacific = set()
        atlantic = set()
        for i in range(rl):
            pacific.add((i,0))
            atlantic.add((i,cl-1))
        for i in range(cl):
            pacific.add((0,i))
            atlantic.add((rl-1,i))
        pacific_reach = set()
        atlantic_reach = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(r,c,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for dr,dc in directions:
                nr = r +dr
                nc = c+dc
                if nr >= rl or nr <0 or nc >= cl or nc <0 or heights[nr][nc] < heights[r][c]:
                    continue
                else:
                    dfs(nr,nc,visited)
        for r,c in pacific:
            dfs(r,c,pacific_reach)
        for r,c in atlantic:
            dfs(r,c,atlantic_reach)
        res =[]
        return [list(cell) for cell in pacific_reach & atlantic_reach]
                
        