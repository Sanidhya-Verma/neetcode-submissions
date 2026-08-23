class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rl = len(board)
        cl = len(board[0])

        border_0 =set()
        for i in range(cl):
            if board[0][i] == 'O':
                border_0.add((0,i))

            if board[rl-1][i] == 'O':
                border_0.add((rl-1,i))
        
        for j in range(1,rl):
            if board[j][0] == 'O':
                border_0.add((j,0))

            if board[j][cl-1] == 'O':
                border_0.add((j,cl-1))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r,c):
            board[r][c] = 's'
            
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if nr >= rl or nr <0 or nc >= cl or nc <0 or board[nr][nc] != 'O':
                    continue
                else:
                    dfs(nr,nc)
        for r,c in border_0:
            dfs(r,c)
        for i in range(rl):
            for j in range(cl):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 's':
                    board[i][j] = 'O'
                

        