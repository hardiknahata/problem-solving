class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minlimit = float('-inf')  # Tracks the lower bound for the current node
        stack = []  # Simulates the stack of the traversal process

        for num in preorder:
            # Pop elements smaller than the current node to find the new lower bound
            while stack and stack[-1] < num:
                minlimit = stack.pop()

            # If the current node is smaller than the minimum limit, the sequence is invalid
            if num < minlimit:
                return False

            # Push the current node onto the stack
            stack.append(num)

        return True  # All nodes satisfy the BST preorder traversal properties

# TC = O(n), where n is the length of the preorder list
# - Each element is pushed and popped from the stack at most once.
# SC = O(n), for the stack used to simulate the traversal process