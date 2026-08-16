class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fmap ={}
        left = 0
        right = 0
        most_comman = 0
        maxcount =0
        while(right<len(s)):
            fmap[s[right]] = fmap.get(s[right],0) +1
            most_comman= max(most_comman,fmap[s[right]])
            if(right-left+1 - most_comman <= k):
                maxcount = max(right-left+1,maxcount)
            else:
                fmap[s[left]] -= 1
                left += 1
            right += 1
        return maxcount







        
                   
        