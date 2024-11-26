class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = maxsum = nums[0]
        
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            maxsum = max(cur, maxsum)
        return maxsum