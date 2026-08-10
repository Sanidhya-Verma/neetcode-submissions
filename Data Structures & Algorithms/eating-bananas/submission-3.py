class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        tot =  sum(piles)
        lo = -(-tot//h)
        hi = max(piles)
        # k can lie between lo and hi so binary search now to find the best k for our ques
        def hour_needed(k) ->int:
            return sum(-(-p//k) for p in piles)

        while lo<=hi:
            m = (lo+hi)//2
            if(hour_needed(m) <= h):
                hi =  m-1
            else:
                lo = m+1
        return lo # almost put return m be careful


        

        