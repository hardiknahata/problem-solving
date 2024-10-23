from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = Counter()
        ans = 0
        
        # Initialize two pointers for the sliding window (left and right)
        left = right = 0

        # Iterate through the string using the right pointer
        while right < len(s):
            # Get the current character at the right pointer
            current_char = s[right]

            # Add or update the count of this character in the window
            counts[current_char] += 1

            # If the character count exceeds 1, it means it's a repeating character
            # So we need to shrink the window from the left until there are no repeats
            while counts[current_char] > 1:
                # Get the character at the left pointer
                left_char = s[left]
                
                # Decrease the count of the left character as we're moving left pointer to the right
                counts[left_char] -= 1

                # Move the left pointer to shrink the window
                left += 1

            # Calculate the current window size (right - left + 1) and update the max length (ans)
            ans = max(ans, right - left + 1)

            # Move the right pointer to expand the window
            right += 1

        # Return the maximum length of substring without repeating characters
        return ans
