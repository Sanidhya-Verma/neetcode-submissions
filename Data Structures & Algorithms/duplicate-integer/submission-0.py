class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for i in nums:
            record[i] = record.get(i,0)+1
        for i in record.values():
            if i>1:
                return True
        return False

        