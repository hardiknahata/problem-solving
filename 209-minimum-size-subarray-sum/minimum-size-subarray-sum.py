class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sumwin = 0
        ans = float('inf')

        for r in range(len(nums)):
            sumwin += nums[r]
            while sumwin >= target:
                len_subarr = r-l+1
                ans = min(ans, len_subarr)
                sumwin -= nums[l]
                l += 1
        
        return ans if ans != float('inf') else 0



