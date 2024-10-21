# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue= collections.deque()
        queue.append(root)
        leftSide = True
        res=[]

        while queue:
            n = len(queue)
            levels = []
            for i in range(n):
                node = queue.popleft()
                levels.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if leftSide:
                res.append(levels)
            else:
                res.append(levels[::-1])

            leftSide = not leftSide
        return res


                

            

        