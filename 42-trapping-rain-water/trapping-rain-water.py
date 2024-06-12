class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prefix_sum = N*[-1]
        suffix_sum = N*[-1]
        trapped = N*[0]

        prefix_sum[0] = height[0]
        suffix_sum[N-1] = height[N-1]

        for i in range(1,N):
            prefix_sum[i] = max(prefix_sum[i-1], height[i])
        
        for i in range(N-2,-1,-1):
            suffix_sum[i] = max(suffix_sum[i+1], height[i])

        for i in range(N):
            trapped[i] = min(prefix_sum[i], suffix_sum[i]) - height[i]
        
        return sum(trapped)

# TC = 3*O(N)
# SC = 2*O(N)       