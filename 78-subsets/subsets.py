class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, cur):
            if len(cur) == self.k:
                self.output.append(cur[:])
                return

            for i in range(first, self.n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        self.output = []
        self.n = len(nums)
        self.k = 0 # size of current subset
        for self.k in range(self.n+1):
            backtrack(0, [])
        
        return self.output
        
