class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch.lower() for ch in s if ch.isalnum()])
        N = len(s) -1
        
        l, r = 0, N

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        