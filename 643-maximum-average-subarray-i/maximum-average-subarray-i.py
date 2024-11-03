class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        
        if k == N:
            return sum(nums)/N

        max_sum = cur_sum = sum(nums[:k])
        for i in range(k,N):
            cur_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum/k
        