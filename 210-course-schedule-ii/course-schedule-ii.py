class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a map from course->pre
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        output = []
        cycle, visited = set(), set()
        def dfs(crs):
            # base cases
            if crs in cycle:
                return False            
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True


        for i in range(numCourses):
            if not dfs(i): return []
        
        return output        