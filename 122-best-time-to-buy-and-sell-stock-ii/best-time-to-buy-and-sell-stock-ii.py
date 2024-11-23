class Solution:
    def maxProfit(self, prices):
        N = len(prices)
        res = 0
        for i in range(1,N):
            if prices[i] > prices[i-1]:
                res += prices[i]-prices[i-1]
        return res
        