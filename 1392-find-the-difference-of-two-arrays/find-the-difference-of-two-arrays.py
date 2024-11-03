class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1_unique = set(nums1)
        n2_unique = set(nums2)
        n1 = [x for x in n1_unique if x not in n2_unique]
        n2 = [x for x in n2_unique if x not in n1_unique]
        
        return [n1, n2]



        


        