class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalindromeFromCenter(s, i, j):
            counts = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                counts +=1
                i -= 1
                j += 1
            return counts
        
        ans = 0
        for i in range(len(s)):
            ans += checkPalindromeFromCenter(s, i, i) # odd
            ans += checkPalindromeFromCenter(s, i, i+1) # even
            
        return ans