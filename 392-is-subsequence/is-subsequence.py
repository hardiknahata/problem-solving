class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False
            
        i = j = 0
        while True:            
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if i == len(s) or j == len(t):
                break
        
        return i == len(s)