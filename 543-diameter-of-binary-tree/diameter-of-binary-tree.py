# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDiameter(self, root, maxi):
        if root is None:
            return 0
        lh = self.findDiameter(root.left, maxi)
        rh = self.findDiameter(root.right, maxi)
        maxi[0] = max(maxi[0], lh+rh)
        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        self.findDiameter(root, maxi)
        return maxi[0]


        