class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # Use a tuple of character counts as the key
            count = [0] * 26  # Assuming only lowercase English letters
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        # Collect and return the grouped anagrams
        return list(anagrams.values())

# TC = O(n * k), where n is the number of words and k is the average word length
# SC = O(n * k), for storing the grouped anagrams and the frequency count keys