class Solution:
    def twoSum(self, numbers: List[int], target: int):
        left = 0
        right = len(numbers)-1
        while (left<right and numbers[left]+numbers[right] != target):
            if(numbers[left]+numbers[right] > target):
                right -= 1
            if(numbers[left]+numbers[right] < target):
                left += 1
        return list((left+1,right+1))
        