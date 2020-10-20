"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
"""
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 804ms 70.67%
        points.sort(key=lambda point:(point[0]**2 +point[1]**2)**(1/2))
        return points[0:K]
        

if __name__ == "__main__":
    points = [[1,3],[-2,2]]
    k = 1
    S = Solution()
    print(S.kClosest(points, k))