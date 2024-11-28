class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map from course->pre
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
    
        visited = set()
        def dfs(crs):
            # base cases
            if crs in visited:
                return False
            if premap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            premap[crs] = []
            return True


        for i in range(numCourses):
            if not dfs(i): return False
        
        return True