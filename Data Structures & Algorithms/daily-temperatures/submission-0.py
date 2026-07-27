class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) != 0 and (temperatures[i] > temperatures[stack[-1]]):
                prev_day_index = stack.pop()
                res[prev_day_index] = i - prev_day_index
            stack.append(i)
        return res