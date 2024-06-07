class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        # 1, 2 ,3
        for j, num in enumerate(digits[::-1]):
            i = N - j -1
            if num < 9:
                digits[i] = num + 1
                break
            else:
                digits[i] = 0
        
        if digits[0] == 0:
            digits.insert(0,1)
        return digits
    
