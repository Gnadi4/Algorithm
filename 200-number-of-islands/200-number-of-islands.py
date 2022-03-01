class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        h = len(grid)
        w = len(grid[0])
        
        def func(grid_tmp, i, j):
            grid_tmp[i][j] = "0"
            if i+1<h and grid_tmp[i+1][j] == "1":
                grid_tmp = func(grid_tmp, i+1, j)
            if j+1<w and grid_tmp[i][j+1] == "1":
                grid_tmp = func(grid_tmp, i, j+1)
            if i-1>=0 and grid_tmp[i-1][j] == "1":
                grid_tmp = func(grid_tmp, i-1, j)
            if j-1>=0 and grid_tmp[i][j-1] == "1":
                grid_tmp = func(grid_tmp, i, j-1)
            
            return grid_tmp
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid = func(grid, i, j)
                    ans += 1
        return ans