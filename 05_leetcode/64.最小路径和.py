#! -*- encoding:utf-8 -*-
"""
@File    :   64.最小路径和.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""

#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List


# @lc code=start
class Solution:
    '''
    思路：动态规划  进行一次遍历 每次更新右下角到当前节点的最短距离
    结果：60ms, 60.86%; 7.51%
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid

        self.distance = [[0]*self.col for _ in range(self.row)]
        for r in range(self.row-1, -1, -1):
            for c in range(self.col-1, -1, -1):
                self.distance[r][c] = self.grid[r][c] + self.shortest(r, c)
        

        return self.distance[0][0]

    def shortest(self, r, c):
        d = []
        if c+1 < self.col:
            d.append(self.distance[r][c+1])
        if r+1 < self.row:
            d.append(self.distance[r+1][c])
        if len(d) > 0:
            return min(d)
        else:
            return 0

# @lc code=end

class Solution_1:
    '''
    思路：图的回溯式深度优先搜索
    结果：outof time
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        else:
            self.row = len(grid)
            self.colum = len(grid[0])

        self.grid = grid
        self.visited = [[False]* self.colum for _ in range(self.row)] # 访问矩阵
        self.src, self.tgt = [0, 0], [self.row-1, self.colum-1] # 源和目标
        self.cur_sum = 0
        self.min_sum = float('inf')

        self.DFS(cur = self.src) # 从源点开始遍历

        return int(self.min_sum)
        

    def DFS(self, cur):
        # 标记访问
        self.visited[cur[0]][cur[1]] = True
        self.cur_sum += self.grid[cur[0]][cur[1]]

        # 判断是否是 tgt
        if cur == self.tgt:
            self.min_sum = min(self.min_sum, self.cur_sum)
        else:
            # 邻接节点 DFS
            nbs = self.next_neighbor(cur)
            for nb in nbs:
                self.DFS(nb)

        # 回溯
        self.visited[cur[0]][cur[1]] = False
        self.cur_sum -= self.grid[cur[0]][cur[1]]

    def next_neighbor(self, cur):
        # 生成器 产生下一个邻居
        direc = ((-1,0), (0,1), (1,0), (0,-1))
        for d in direc:
            cur_cp = cur[::]
            cur_cp[0] += d[0]
            cur_cp[1] += d[1]
            if 0<= cur_cp[0] < self.row and 0<= cur_cp[1] < self.colum:
                if self.visited[cur_cp[0]][cur_cp[1]] is False:
                    yield cur_cp

if __name__ == "__main__":
    # test_case = [[1,3,1,2],[1,5,1,2],[4,2,1,4],[2,3,6,8]]
    test_case = [[1,3,1],[1,5,1],[4,2,1]]
    # Solution = Solution_1
    S = Solution()
    print(S.minPathSum(test_case))