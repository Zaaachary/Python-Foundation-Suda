#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

from typing import List
# @lc code=start
class Solution:
    '''
    94.88% 78.4%  a.使用visit矩阵  b. 访问过的土地置零
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        if len(grid) == 0:
            return max_island
        col, row = len(grid), len(grid[0])
        visit = [[False for _ in range(row)] for _ in range(col)]
        for c in range(col):
            for r in range(row):
                if not visit[c][r] and grid[c][r] == 1:
                    area = self.BFS(c, r, grid, visit)
                    max_island = max(max_island, area)
        return max_island
    
    @staticmethod
    def BFS(col, row, grid, visit):
        area = 0
        queue = list()
        queue.append((col, row))
        while len(queue) != 0:
            col, row = queue.pop(0)
            if visit[col][row]:
                continue
            else:
                visit[col][row] = True
                area += 1
                for c, r in [(col+1, row),(col-1, row),(col, row+1),(col, row-1)]:
                    if 0 <= c < len(grid) and 0 <= r < len(grid[0]) and grid[c][r] == 1:
                        queue.append((c,r))

        return area
# @lc code=end

class Solution2:
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

