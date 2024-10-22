from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        np = len(p)
        ns = len(s)
        if ns < np:
            return []

        res = []
        p_counts = [0]*26
        for ch in p:
            p_counts[ord(ch)-ord('a')] += 1

        s_counts = [0]*26

        for i in range(ns):
            ch = s[i]
            s_counts[ord(ch)-ord('a')] += 1

            if i >= np:
                s_counts[ord(s[i-np]) - ord('a')] -= 1

            if p_counts == s_counts:
                res.append(i - np + 1)

        return res
