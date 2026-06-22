class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record = {}
        memo = {}
        ans = ""
        min_len = float('inf')
        for i in t :
            record[i] = record.get(i,0)+1
        left =  0
        right = 0
        while(right < len(s)):
            flag = 1
            memo[s[right]] = memo.get(s[right],0)+1
            for i in t:
                if(record[i] > memo.get(i,0)):
                    flag = 0
            if(flag == 1):
                while s[left] not in record or memo[s[left]] > record[s[left]]:
                    memo[s[left]] = memo.get(s[left],0)-1
                    if (memo[s[left]] == 0):
                        del memo[s[left]]
                    left += 1

                current_len =right -left +1
                if current_len <min_len:
                    min_len =current_len    
                    ans =s[left : right+1]
            right += 1
        return ans

            
            
            
            
        