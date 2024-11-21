class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome_from_center(l, r):
            # Expand outward as long as the substring is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Return the valid palindrome substring
            return s[l + 1:r]
        
        longest = ""  # Initialize the longest palindrome found
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_pal = check_palindrome_from_center(i, i)
            # Check for even-length palindromes
            even_pal = check_palindrome_from_center(i, i + 1)
            # Update the longest palindrome found
            longest = max(longest, odd_pal, even_pal, key=len)

        return longest