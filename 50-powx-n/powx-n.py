class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0: return 1  # Base case: any number to the power of 0 is 1
            if x == 0: return 0  # Edge case: 0 raised to any power is 0

            res = power(x, n // 2)  # Recursively compute for half the exponent
            res = res * res  # Square the result
            return x * res if n % 2 else res  # If n is odd, multiply by x
        
        res = power(x, abs(n))  # Compute power for the absolute value of n
        return res if n >= 0 else 1 / res  # If n is negative, return the reciprocal

# TC = O(log n), where n is the absolute value of the exponent (due to halving in each recursive call)
# SC = O(log n), for the recursive call stack