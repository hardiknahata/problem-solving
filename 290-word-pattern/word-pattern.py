class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mapper = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
            
        for ch, string in zip(pattern, s):
            if ch not in mapper:
                if string not in mapper.values():
                    mapper[ch] = string
                else:
                    return False
            else:
                if mapper[ch] == string:
                    pass
                else:
                    return False
        return True
                

