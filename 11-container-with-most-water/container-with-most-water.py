class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        maxarea = 0
        left = 0
        right = N - 1
        
        while left < right:
            h_left, h_right = height[left], height[right]
            cur_area = (right-left) * min(h_left, h_right)
            maxarea = max(maxarea, cur_area)

            if h_left <= h_right:
                left +=1
            else:
                right -= 1
        
        return maxarea

        
        