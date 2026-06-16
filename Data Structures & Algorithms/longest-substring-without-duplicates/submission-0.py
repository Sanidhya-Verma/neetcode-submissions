class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        right =0
        count =0
        if(len(s) ==1 ):
            return 1
        maxcount =0
        while(right < len(s)):
            for i in range(left,right):
                if (s[i] == s[right]):
                    left = i+1
                    break
            right += 1
            maxcount = max(right-left,maxcount)

        return maxcount
            