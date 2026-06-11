class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        if nums[0] > 0 and nums[-1] > 0:
            return []
        if nums[0] < 0 and nums[-1] < 0:
            return []
        for i in range(len(nums)):
            if nums[i] > 0:
                break          
            if i > 0 and nums[i] == nums[i-1]:
                continue     
            a = nums[i]
            left = i + 1
            right = len(nums) - 1 
            while left < right:
                current_sum = a + nums[left] + nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    results.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return results
        