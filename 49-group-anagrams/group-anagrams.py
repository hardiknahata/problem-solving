class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Dictionary to group anagrams by a unique key
        
        for word in strs:
            count = [0] * 26  # Frequency array for characters 'a' to 'z'
            for ch in word:
                count[ord(ch) - ord('a')] += 1  # Increment frequency for each character
            anagrams[tuple(count)].append(word)  # Use tuple of counts as key
        
        return list(anagrams.values())  # Return grouped anagrams as a list

# TC = O(n * k), where n is the number of words and k is the maximum length of a word
# SC = O(n * k), for storing the frequency count keys and grouped anagrams