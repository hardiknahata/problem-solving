from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            pattern = sorted(list(word))
            pattern_str = "".join(pattern)
            anagrams[pattern_str].append(word)

        ans = []
        for groups in anagrams.values():
            ans.append(groups)
        return ans