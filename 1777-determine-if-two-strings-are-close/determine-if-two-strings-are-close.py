class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = [0]*26
        c2 = [0]*26
        
        for ch in word1:
            c1[ord(ch) - ord('a')] += 1
        
        for ch in word2:
            c2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (c1[i]==0 and c2[i]>0) or (c2[i]==0 and c1[i]>0):
                return False

        c1.sort()
        c2.sort()
        return c1 == c2