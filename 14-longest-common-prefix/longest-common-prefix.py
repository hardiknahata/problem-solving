class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        
        # Iterate through the rest of the strings
        for string in strs[1:]:
            # Shorten the prefix until it matches the beginning of string
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

