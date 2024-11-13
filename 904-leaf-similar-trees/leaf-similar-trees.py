# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, seq):
        if root is None:
            return
        self.dfs(root.left, seq)
        self.dfs(root.right, seq)

        if root.left is None and root.right is None:
            seq.append(root.val)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []
        self.dfs(root1, seq1)
        self.dfs(root2, seq2)
        
        return seq1 == seq2