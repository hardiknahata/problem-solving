from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        
        chars_count = Counter(chars)
        for word in words:
            word_count = Counter(word)

            good = True
            for c, freq in word_count.items():
                if chars_count[c] < freq:
                    good = False
                    
            if good:
                ans += len(word)

        return ans


            

            