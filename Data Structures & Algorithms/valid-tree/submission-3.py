from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # i could not think of this edge number optimization - Very Imp good shit 
        if len(edges)!= n-1:
            return False
        
        if edges == [] and n ==1 : # to handle this case 
            return True 

        tree = defaultdict(list)

        for i in range (n):
            tree[i] = []

        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)

        visited = set()

        def dfs(u,parent):
            if u in visited:
                return False
            
            if tree[u] == []:
                return True

            visited.add(u)

            for neigh in tree[u]:
                if neigh == parent:
                    continue
                if dfs(neigh,u) == False:
                    return False
            return True
        
        dfs(0,-1)

        if len(visited) != n :
            return False # to take care of isolated node case 

        return True


        