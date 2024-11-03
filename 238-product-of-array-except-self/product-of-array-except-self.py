class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = n*[0]

        left[0]=1

        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        
        ans = [0]*n
        R = 1

        for i in reversed(range(n)):
            ans[i] = R * left[i]
            R *= nums[i] 

        return ans



# TC: O(N)
# SC: O(1)