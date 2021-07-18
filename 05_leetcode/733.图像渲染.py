#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
from typing import List
import collections

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        91.07% 18.19%
        '''
        targetColor = image[sr][sc]
        if targetColor == newColor:
            return image

        visit = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        queue = list()
        queue.append((sr, sc))
        while len(queue) > 0:
            row, col = queue.pop(0)
            if 0 <= row < len(image) and 0 <= col < len(image[0]):
                if visit[row][col] == True:
                    continue
                elif image[row][col] == targetColor:
                    visit[row][col] = True
                    image[row][col] = newColor
                    queue.append((row+1, col))
                    queue.append((row, col+1))
                    queue.append((row-1, col))
                    queue.append((row, col-1))
        return image


# # @lc code=end

#     def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         currColor = image[sr][sc]
#         if currColor == newColor:
#             return image
        
#         n, m = len(image), len(image[0])
#         que = collections.deque([(sr, sc)])
#         image[sr][sc] = newColor
#         while que:
#             x, y = que.popleft()
#             for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#                 if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
#                     que.append((mx, my))
#                     image[mx][my] = newColor
        
#         return image
