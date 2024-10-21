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

        queue = deque([root])
        res = []
        leftSide = True

        while queue:
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append levels in the desired order
            res.append(levels if leftSide else levels[::-1])
            leftSide = not leftSide

        return res


                

            

        