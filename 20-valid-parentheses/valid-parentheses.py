class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "{":"}",
            "(":')',
            "[":"]"
        }

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if not stack or mapping[stack[-1]] != ch:
                    return False
                stack.pop()
            
        return len(stack)==0