class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        if not grid:
            return ret
        
        def search(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                return 0
            
            # set the value as seen so it doesn't get explored again
            grid[row][col] = 0
            area = 1
            area += search(row+1, col)
            area += search(row-1, col)
            area += search(row, col+1)
            area += search(row, col-1)
            return area
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if val is 1, run dfs
                if grid[row][col] == 1:
                    island_size = search(row,col)
                    ret = max(island_size, ret)

        return ret