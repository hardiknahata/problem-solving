class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for ch_idx in range(len(strs[0])):
            ch = strs[0][ch_idx]

            for j in range(1, len(strs)):
                if ch_idx == len(strs[j]) or strs[j][ch_idx] != ch:
                    return strs[0][:ch_idx]
        
        return strs[0]
        
