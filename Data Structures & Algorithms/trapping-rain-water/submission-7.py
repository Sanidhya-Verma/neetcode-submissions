class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        # 1. Build the Left Cheat Sheet (Walk left to right)
        # What is the tallest wall seen to my left so far?
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
            
        # 2. Build the Right Cheat Sheet (Walk right to left)
        # What is the tallest wall seen to my right so far?
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
            
        # 3. Calculate Water (Your exact masterpiece math!)
        total_water = 0
        for i in range(n):
            # Instant O(1) lookup instead of sending scouts out
            water_level = min(max_left[i], max_right[i]) - height[i]
            total_water += max(0, water_level)
            
        return total_water
        