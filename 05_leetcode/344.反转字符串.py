#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        85.13 %, 6.71 %
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # s.reverse()  # 97.56% 6.35%

# @lc code=end

