# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0

        def findDiameter(root):
            nonlocal maxi
            if root is None:
                return 0
            lh = findDiameter(root.left)
            rh = findDiameter(root.right)
            maxi = max(maxi, lh+rh)
            return 1 + max(lh, rh)            

        findDiameter(root)
        return maxi


        