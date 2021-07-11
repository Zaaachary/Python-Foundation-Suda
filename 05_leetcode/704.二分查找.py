#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            temp = nums[mid]
            if temp == target:
                return mid
            elif temp > target:
                right = mid-1
            else:
                left = mid+1
        else:
            return -1

# @lc code=end

if __name__ == "__main__":
    S = Solution()
    print(S.search([-1,0,3,5,9,12], 2))
    print(S.search([-1,0,3,5,9,12], 9))
    print(S.search([-1,0,3,5,9,12], 0))
