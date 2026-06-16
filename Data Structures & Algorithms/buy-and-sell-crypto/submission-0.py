class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if (maxprofit < prices[j] - prices[i]):
                    if(prices[j]<prices[j-1]):
                        continue
                    maxprofit = prices[j] - prices[i]
        return maxprofit
                    
                
        