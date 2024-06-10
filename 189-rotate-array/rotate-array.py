class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # since k can be beyond N
        k %= len(nums)

        # reverse array
        x = nums[::-1]

        # reverse first k
        y = x[:k][::-1]

        # reverse remaining after kth
        z = x[k:][::-1]

        # join
        x = y + z
        nums[:] = x
        