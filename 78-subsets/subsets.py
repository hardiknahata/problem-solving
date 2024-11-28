class Solution:
    def subsets(self, nums):
        def backtrack(first, curr):
            # Base case: if the current subset size equals k, add it to the output
            if len(curr) == self.k:
                self.output.append(curr[:])  # Make a copy of the current subset
                return  # End the recursion for this path

            # Iterate over the remaining elements starting from 'first'
            for i in range(first, self.n):
                curr.append(nums[i])  # Include nums[i] in the current subset
                backtrack(i + 1, curr)  # Recurse with the next elements
                curr.pop()  # Remove nums[i] to explore other subsets

        self.output = []  # List to store all subsets
        self.n, self.k = len(nums), None  # n: total number of elements in nums, k: size of current subset
        for self.k in range(self.n + 1):  # Iterate over all possible subset sizes (0 to n)
            backtrack(0, [])  # Start backtracking with an empty subset
        return self.output  # Return all subsets

# TC: O(N*2^N)
# SC: O(N) + O(2^N)