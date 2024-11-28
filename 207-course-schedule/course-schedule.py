class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a map from course -> list of prerequisites
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
    
        cycle = set()  # Track courses in the current DFS path

        def dfs(crs):
            # If the course is already in the current DFS path, there is a cycle
            if crs in cycle:
                return False
            # If the course has no prerequisites, it can be finished
            if premap[crs] == []:
                return True
            
            cycle.add(crs)  # Mark the course as part of current cycle
            for pre in premap[crs]:  # Check all prerequisites of this course
                if not dfs(pre): 
                    return False  # Return False if any prerequisite cannot be finished
            cycle.remove(crs)  # Remove the course from the current path
            premap[crs] = []  # Mark the course as processed (no more prerequisites)
            return True

        # Check all courses to ensure they can be finished
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True  # All courses can be finished

# TC = O(n + p), where n is the number of courses and p is the number of prerequisites
# - Each course and prerequisite is visited once.
# SC = O(n + p), for the adjacency list (premap) and the recursion stack in the worst case
