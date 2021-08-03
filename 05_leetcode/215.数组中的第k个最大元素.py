#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
from typing import List
class Solution:
    # 86.27%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k):
            result = heapq.heappop(heap)
        return -result



if __name__ == "__main__":
    pass
# @lc code=end