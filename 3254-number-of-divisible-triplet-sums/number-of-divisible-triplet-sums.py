from collections import defaultdict
from typing import List

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        # Dictionary to count the frequency of remainders when elements are divided by d
        remainder_count = defaultdict(int)
        triplet_count = 0  
        n = len(nums)

        # Iterate over the array, considering each element as the middle element of a potential triplet
        for j in range(n):
            # For each element nums[j], consider all elements nums[k] that come after it
            for k in range(j + 1, n):
                # Calculate the remainder needed from nums[i] to make the triplet sum divisible by d
                required_remainder = (d - (nums[j] + nums[k]) % d) % d
                # Add the number of times this required remainder has occurred before index j
                triplet_count += remainder_count[required_remainder]
            # Update the remainder count for the current element nums[j]
            current_remainder = nums[j] % d
            remainder_count[current_remainder] += 1

        return triplet_count

# TC: O(n^2)
# SC: O(d) space