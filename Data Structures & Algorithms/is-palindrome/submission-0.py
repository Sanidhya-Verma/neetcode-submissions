def lowered (s: str):
    lower_s =""
    for i in s:
        if i.isalnum():
            lower_s += i.lower()
    return lower_s
class Solution:
    def isPalindrome(self, s: str):
        s_lower = lowered(s)
        j = len(s_lower) -1
        for i in range(len(s_lower)):
            if(s_lower[i]==s_lower[j]):
                j -= 1
            else:
                return False
        return True