class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        for i in range(len(word1)):
            if i > len(word2)-1:
                break
            res += word1[i] + word2[i]
        
        if len(word2) >= len(word1):
            res += word2[i+1:]
        else:
            res += word1[i:]
        
        return res

