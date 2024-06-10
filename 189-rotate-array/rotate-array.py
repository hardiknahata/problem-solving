class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        x = N*[0]
        for i in range(N):
            x[(i+k) % N] = nums[i]

        nums[:] = x
        