class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n1 = n2 = float('inf')

        for num in nums:
            if num <= n1:
                n1 = num
            elif num <= n2:
                n2 = num
            else:
                return True

        return False
            