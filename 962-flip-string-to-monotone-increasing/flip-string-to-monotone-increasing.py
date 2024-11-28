class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Count the total number of '0's in the string
        total_zeros = sum(1 for c in s if c == '0')

        # Initialize flips_needed to flip all '0's to '1's
        flips_needed = total_zeros

        # Track the minimum flips required
        min_flips = flips_needed

        # Traverse the string to adjust flips dynamically
        for char in s:
            if char == '0':
                # Decrement flips_needed as we don't need to flip this '0'
                flips_needed -= 1
            else:
                # Increment flips_needed as we now need to flip this '1'
                flips_needed += 1
            
            # Update the minimum flips required
            min_flips = min(min_flips, flips_needed)

        return min_flips  # Return the minimum flips required

# TC = O(n), where n is the length of the string
# - First pass to count '0's and second pass to adjust flips dynamically.
# SC = O(1), no additional data structures used.