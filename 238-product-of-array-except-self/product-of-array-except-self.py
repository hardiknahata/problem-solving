class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N  # Initialize the result array
        ans[0] = 1  # The product of all elements to the left of the first element is 1
        
        # Compute the left product for each element
        for i in range(1, N):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        R = 1  # Initialize the right product
        # Compute the product of all elements to the right
        for i in reversed(range(N)):
            ans[i] = ans[i] * R  # Multiply the left product with the right product
            R = R * nums[i]  # Update the right product
        
        return ans  # Return the result array

# TC = O(n), two passes through the nums array
# SC = O(1), excluding the output array (ans) as the problem specifies constant extra space