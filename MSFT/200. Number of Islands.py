# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from collections import deque
class Solution:
    def numIslands(self, grid):
        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.helper(grid,queue) # turn the adjancent '1' to '0'
                    count += 1
        print(grid)
        return count
    
    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0 #0