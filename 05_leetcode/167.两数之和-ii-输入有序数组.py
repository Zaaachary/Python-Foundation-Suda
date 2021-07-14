#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        99.17%, 5.25%
        [1,2,3,4,5,9]  11
        '''
        left, right = 0, len(numbers)-1
        while left <= right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return left+1, right+1


# @lc code=end

