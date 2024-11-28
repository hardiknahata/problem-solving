from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        R, C = len(rooms), len(rooms[0])

        # Add all gates to the queue
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movement directions

        while queue:
            r, c = queue.popleft()  # Process the next cell
            for dx, dy in directions:
                nr, nc = r + dx, c + dy  # Calculate neighbor coordinates
                # Skip invalid or already processed cells
                if nr < 0 or nr >= R or nc < 0 or nc >= C or rooms[nr][nc] != 2147483647:
                    continue
                rooms[nr][nc] = rooms[r][c] + 1  # Update distance for empty room
                queue.append((nr, nc))  # Add the updated room to the queue

# TC = O(m * n)
# SC = O(m * n), for the queue used in BFS in the worst case.
