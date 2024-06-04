class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        for word in words[::-1]:
            result += word + " "
        
        return result.strip()