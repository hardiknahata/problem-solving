class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        if t == "" and s!="":
            return False
    
        if len(s) > len(t):
            return False
        
        l = 0
        r = 0
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        
        return l == len(s)

                
        


        