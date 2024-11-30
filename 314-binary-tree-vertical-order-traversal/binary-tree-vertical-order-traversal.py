# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tracker = defaultdict(list)

        queue = deque()
        queue.append((0, root))

        while len(queue) > 0:
            col, node = queue.popleft()
            if node:
                tracker[col].append(node.val)
                queue.append((col-1, node.left))
                queue.append((col+1, node.right))
        
        return [tracker[x] for x in sorted(tracker.keys())]