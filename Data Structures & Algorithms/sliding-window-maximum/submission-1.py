class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        ans = []
        left = 0
        right  = k -1
        for i in range(left,right):
            heapq.heappush(heap, (-1*nums[i], i))
        while (right < len(nums)):
            heapq.heappush(heap, (-1*nums[right], right))
            while (heap[0][1] < left):
                heapq.heappop(heap)
            ans.append(-1*heap[0][0])
            left += 1
            right += 1
            
        return ans
            
        
        