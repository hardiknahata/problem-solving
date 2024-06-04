class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we will use 3 pointers
        # i - insert, j - finder, count - count
        count = 1
        i = 1

        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                if count < 2:
                    nums[i] = nums[j]
                    i += 1
                count += 1
            else:
                count = 1
                nums[i] = nums[j]
                i += 1
        return i

#Time Complexity: O(N) since we process each element exactly once
# Space Complexity: O(1)