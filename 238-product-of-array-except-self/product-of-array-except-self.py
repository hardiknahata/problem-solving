class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        ans = [0] * N
        left = [0] * N
        right = [0] * N
        
        left[0], right[N-1] = 1, 1
        
        # construct left products
        for i in range(1, N):
            left[i] = left[i-1] * nums[i-1]
        
        # construct right products
        for i in range(N-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # construct answer
        for i in range(N):
            ans[i] = left[i] * right[i]
        
        return ans

