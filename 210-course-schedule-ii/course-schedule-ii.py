class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a map from course -> list of prerequisites
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        output = []  # List to store the course order
        cycle, visited = set(), set()  # Track nodes in the current path (cycle detection) and fully processed nodes

        def dfs(crs):
            # If the course is already in the current DFS path, there is a cycle
            if crs in cycle:
                return False
            # If the course has already been processed, skip it
            if crs in visited:
                return True
            
            cycle.add(crs)  # Add course to the current path
            for pre in premap[crs]:  # Process all prerequisites
                if not dfs(pre): 
                    return False  # Return False if any prerequisite causes a cycle
            cycle.remove(crs)  # Remove course from the current path
            visited.add(crs)  # Mark the course as fully processed
            output.append(crs)  # Add the course to the output in reverse order
            return True

        # Check all courses to ensure they can be finished
        for i in range(numCourses):
            if not dfs(i):
                return []  # Return an empty list if any course causes a cycle
        
        return output  # Return the course order in reverse topological order

# TC = O(n + p), where n is the number of courses and p is the number of prerequisites
# - Building the adjacency list (premap) takes O(p).
# - Each course and prerequisite is visited once during DFS.
# SC = O(n + p), for the adjacency list (premap), cycle/visited sets, and the recursion stack
