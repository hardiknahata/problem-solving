class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        e = None
        c = 0
        for i in range(len(nums)):
            # print(f"i:{i} e:{e} c:{c}")
            if c == 0:
                e = nums[i]
            
            if nums[i] != e:
                c -= 1

            else:
                c += 1
        
        return e
                