class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        maxlen = 0
        l=r=0

        for r in range(len(s)):
            ch = s[r]
            counter[ch] +=1
            # print(l,r) 
            while counter[ch] > 1:
                counter[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r-l+1)
        
        return maxlen
        