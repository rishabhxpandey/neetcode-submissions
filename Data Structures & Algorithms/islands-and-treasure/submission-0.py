from collections import deque
import copy
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        [X, -1 , 0,  X]
        [X,  X,  X, -1]
        [X, -1,  X, -1]
        [0, -1,  X,  X]

        from each treasure chest, do a BFS out and populate the grid for the length of path to the chest
        if another BFS yields a smaller value, replace it
        '''
        INF = 2**31 - 1

        def search(row, col):
            visited = set()
            visited.add((row, col))

            if grid[row][col] == -1:
                return

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([(row,col)])
            distance = 1

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for r, c in directions:
                        nr, nc = row + r, col + c
                        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                            continue
                        if grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr,nc) in visited:
                            continue

                        
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        grid[nr][nc] = min(grid[nr][nc], distance)

                distance += 1


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    search(row, col)