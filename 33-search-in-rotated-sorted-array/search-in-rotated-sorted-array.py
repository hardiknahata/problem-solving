from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Step 1: Find the pivot where the rotation happens
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:  # Pivot is in the right half
                left = mid + 1
            else:  # Pivot is in the left half
                right = mid - 1
        
        # Step 2: Define binary search for searching within a range
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:  # Found the target
                    return mid
                elif nums[mid] > target:  # Target is in the left half
                    right = mid - 1
                else:  # Target is in the right half
                    left = mid + 1
            return -1  # Target not found

        # Step 3: Search in both halves (split by the pivot)
        # Search in the left sorted portion
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer
        
        # If not found, search in the right sorted portion
        return binarySearch(left, len(nums) - 1, target)

# TC: O(log n) - Two binary searches: one to find the pivot and another to search in a half.
# SC: O(1) - Constant space usage.