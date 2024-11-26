class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = maxsum = nums[0]  # Initialize current sum and max sum with the first element

        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])  # Choose to continue with the current subarray or start fresh
            maxsum = max(maxsum, cur)  # Update the maximum subarray sum

        return maxsum  # Return the largest subarray sum