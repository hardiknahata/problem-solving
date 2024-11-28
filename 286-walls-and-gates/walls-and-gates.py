from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        R, C = len(rooms), len(rooms[0])

        # add all gates to queue
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if nr < 0 or nr >= R or nc < 0 or nc >= C or rooms[nr][nc]!= 2147483647:
                    continue
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr,nc))


        

