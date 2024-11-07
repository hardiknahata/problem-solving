class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_win = num_zeros = 0
        l = 0

        N = len(nums)

        for r in range(N):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            max_win = max(max_win, r-l+1)
        
        return max_win