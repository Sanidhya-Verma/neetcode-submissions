from collections import defaultdict 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(curr,target,visited):
            if curr == target : return True

            visited.add(curr)

            for neigh in graph[curr]:
                if neigh not in visited:
                    if dfs(neigh,target,visited) == True:
                        return True
            return False

        for u,v in edges:
            visited = set()

            if dfs(u,v,visited) == True:
                return [u,v]

            graph[u].append(v)
            graph[v].append(u)

        


        

        
        