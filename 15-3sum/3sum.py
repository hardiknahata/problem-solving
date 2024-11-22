class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array to enable two-pointer technique

        triplets = []  # Result list to store unique triplets
        for i in range(len(nums) - 2):
            # Skip duplicates for the current element nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1  # Initialize left pointer
            r = len(nums) - 1  # Initialize right pointer
            while l < r:
                total = nums[l] + nums[r] + nums[i]  # Calculate the sum of the triplet
                
                if total > 0:  # If the total is too large, move the right pointer left
                    r -= 1
                elif total < 0:  # If the total is too small, move the left pointer right
                    l += 1
                else:  # Found a valid triplet
                    triplets.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for nums[l]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip duplicates for nums[r]
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1  # Move left pointer for the next potential triplet
                    r -= 1  # Move right pointer for the next potential triplet

        return triplets

# TC = O(n^2), where n is the length of the input array
# - Sorting takes O(n log n)
# - The outer loop runs O(n) times, and the two-pointer search runs O(n) in the worst case.
# SC = O(1), excluding the space required for the output list