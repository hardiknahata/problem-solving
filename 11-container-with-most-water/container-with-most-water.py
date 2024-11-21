class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0
        N = len(height)
        r = N-1

        while l<r:
            left = height[l]
            right = height[r]
            area = min(left, right)* (r-l)
            maxarea = max(area, maxarea)
            if left < right:
                l +=1
            else:
                r-= 1
        return maxarea
