from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tracker = defaultdict(list)  # Tracks nodes column-wise
        queue = deque()  # Queue for BFS
        queue.append((0, root))  # Start BFS with root at column 0

        while queue:
            col, node = queue.popleft()
            if node:
                tracker[col].append(node.val)  # Add node value to its column
                queue.append((col - 1, node.left))  # Add left child to column -1
                queue.append((col + 1, node.right))  # Add right child to column +1

        # Return the values column-wise in sorted order of columns
        return [tracker[x] for x in sorted(tracker.keys())]

# TC: O(NlogN) - Each node is visited once in BFS traversal which is O(N), and sorting keys is O(NlogN)

# SC: O(n) - Space for tracker and queue, where tracker stores nodes for each column and queue stores nodes during traversal.