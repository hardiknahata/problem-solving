from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        for ch in ransomNote:
            if mag[ch] <= 0:
                return False
            mag[ch] -= 1

        return True