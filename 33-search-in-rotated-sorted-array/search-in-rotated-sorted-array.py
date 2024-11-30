class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid -1
        
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if (answer := binarySearch(0, left-1, target)) != -1:
            return answer
        
        return binarySearch(left, len(nums)-1, target)

