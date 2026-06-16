class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        sum = 0
        for i in range(r):
            maxleft = 0
            maxright = 0
            for j in range(l,i):
                maxleft = max(maxleft,height[j])
            for j in range(i+1,r+1):
                maxright = max(maxright,height[j])
            height_at_i = max(0,min(maxleft,maxright)-height[i])
            sum += height_at_i
        return sum
            

        
        