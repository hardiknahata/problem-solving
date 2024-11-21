class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array, dp[0] = 1 as the base case
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        # Iterate through each coin
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]  # Update dp[a] with combinations using 'coin'
        
        return dp[amount]  # Return the number of ways to make 'amount'

# TC = O(n * m), where n = amount, m = number of coins
# SC = O(n), where n = amount (for the dp array)