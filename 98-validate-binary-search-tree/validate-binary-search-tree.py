# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkBST(self, root, minVal, maxVal):
        if root==None:
            return True
        
        if (root.val >= maxVal or root.val <= minVal):
            return False
        
        return (self.checkBST(root.left, minVal, root.val) and self.checkBST(root.right, root.val, maxVal))
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float(-inf), float(inf))
        
            
        
        