# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def getMaxPath(root):
            nonlocal maxSum

            if root is None:
                return 0

            lsum = max(0, getMaxPath(root.left))
            rsum = max(0, getMaxPath(root.right))
            
            total = root.val + lsum + rsum
            maxSum = max(maxSum, total)

            return max(lsum, rsum) + root.val
        
        getMaxPath(root)
        return maxSum

        