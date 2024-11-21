class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value greater than the maximum amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        # Iterate through all amounts from 1 to the target amount
        for a in range(1, amount + 1):
            # Check each coin to see if it can contribute to the current amount
            for c in coins:
                if a - c >= 0:  # Ensure the coin does not make the amount negative
                    dp[a] = min(1 + dp[a - c], dp[a])  # Update dp with the minimum coins needed
        
        # Return the result; if it's unchanged, return -1 (not possible)
        return dp[amount] if dp[amount] != amount + 1 else -1