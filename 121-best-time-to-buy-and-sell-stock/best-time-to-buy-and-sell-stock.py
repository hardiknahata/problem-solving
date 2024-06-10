class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
            # print(f"i:{i} min_price:{min_price} max_profit:{max_profit}")
        return max_profit

            


        