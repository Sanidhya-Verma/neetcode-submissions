class Solution:
    def find_ancestor(self,family,u):
        while True:
            v = family[u] 
            if v == u:
                return v
            else: return self.find_ancestor(family,v)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        family = {i:i for i in range(n)}
        for u,v in edges:
            ancestor_u = self.find_ancestor(family,u)
            ancestor_v = self.find_ancestor(family,v)

            if ancestor_u != ancestor_v:
                family[ancestor_u] = ancestor_v

            else:
                continue # cycle here btw

        ans = 0
        for i in range(n):
            if family[i] == i:
                ans+=1
        return ans
            



                