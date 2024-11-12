class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # apply 2 sum logic and find no of pairs that sum to k -> ans
        hm = {}
        ans = 0
        for i, num in enumerate(nums):
            comp = k - num
            if comp in hm and hm[comp]>0:
                hm[comp] -= 1
                ans += 1
            else:
                if num in hm:
                    hm[num] += 1
                else:
                    hm[num] = 1
        
        return ans

        