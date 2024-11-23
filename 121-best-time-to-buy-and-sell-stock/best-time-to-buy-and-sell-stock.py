class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the lowest price to buy
        max_profit = 0  # Track the maximum profit

        for price in prices:
            if price < min_price:  # Update the lowest buying price
                min_price = price
            else:  # Calculate profit and update max profit
                max_profit = max(max_profit, price - min_price)

        return max_profit  # Return the maximum profit

# TC = O(n), single pass through the prices list
# SC = O(1), constant space used