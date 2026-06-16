class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        record ={}
        left = 0
        right = 0
        maxf = 0
        maxcount =0
        while(right<len(s)):
            record[s[right]] = record.get(s[right],0) +1
            maxf = max(maxf,record[s[right]])
            if(right-left+1 - maxf <= k):
                maxcount = max(right-left+1,maxcount)
            else:
                record[s[left]] -= 1
                left += 1
            right += 1
        return maxcount







        
                   