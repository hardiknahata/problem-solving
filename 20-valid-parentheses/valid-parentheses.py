class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stack to track unmatched opening brackets
        mapping = {  # Mapping of opening to closing brackets
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for ch in s:
            if ch in mapping:  # If it's an opening bracket, push to stack
                stack.append(ch)
            else:  # If it's a closing bracket
                # Check if the stack is empty or the top of the stack doesn't match
                if not stack or mapping[stack[-1]] != ch:
                    return False
                stack.pop()  # Pop the matched opening bracket
            
        return len(stack) == 0  # Valid if no unmatched brackets remain

# TC = O(n), where n is the length of the string; each character is processed once
# SC = O(n), for the stack in the worst case when all characters are opening brackets