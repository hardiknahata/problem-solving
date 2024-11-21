class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = collections.defaultdict(int)
        maxlen = 0
        l = r = 0
        
        while r < len(s):
            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r-l+1)
            r += 1

        return maxlen
        