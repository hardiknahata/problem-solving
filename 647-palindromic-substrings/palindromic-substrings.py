class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalindromeFromCenter(s, i, j):
            counts = 0
            # Expand outward from the center and count palindromic substrings
            while i >= 0 and j < len(s) and s[i] == s[j]:
                counts += 1
                i -= 1
                j += 1
            return counts
        
        ans = 0
        for i in range(len(s)):
            ans += checkPalindromeFromCenter(s, i, i)  # Count odd-length palindromes
            ans += checkPalindromeFromCenter(s, i, i + 1)  # Count even-length palindromes
            
        return ans  # Return total count of palindromic substrings

# TC = O(n^2), where n is the length of the string
# - Outer loop runs O(n), and inner palindrome expansion takes O(n) in the worst case.
# SC = O(1), constant space is used