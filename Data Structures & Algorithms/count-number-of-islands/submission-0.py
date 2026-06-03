class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        approach:
        - counter to track islands
        - some graph traversal algo (bfs/dfs)
        - have a 'visited' set

        iterate over each spot
        - if spot is land and not in visited, dfs
        - else continue
        '''

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(row, col):
            if (row,col) in visited:
                return
            visited.add((row,col))
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    if grid[new_row][new_col] == "0":
                        continue
                    dfs(new_row, new_col)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                   islands += 1
                   dfs(row, col)   
        
        return islands

