class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            # print(f"i={i} len={len(nums)} nums = {nums}")
            if i==len(nums) or i > len(nums):
                break
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)