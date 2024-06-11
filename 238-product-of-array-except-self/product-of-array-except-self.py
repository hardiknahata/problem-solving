class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        ans = [0] * N
        
        ans[0] = 1
        
        # construct left products in ans
        for i in range(1, N):
            ans[i] = ans[i-1] * nums[i-1]

        # right product variable
        R = 1

        # construct answer
        for i in reversed(range(N)):
            ans[i] = ans[i] * R
            R *= nums[i]
        
        return ans

# TC: O(N)
# SC: O(1)