#! -*- encoding:utf-8 -*-
"""
@File    :   53.最大子序和.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List

# @lc code=start
class Solution:
    def maxSubArray_org(self, nums: List[int]) -> int:
        '''
        76.21 %
        思路
            滑窗遍历列表；
            sum < 0 时候 left+1 直到 与right重合；
            right + 1，重新计算 current 值；
        '''
        if len(nums) == 0:
            return 
        left = 0
        current, maxsum = 0, nums[0]
        for right in range(len(nums)):
            current += nums[right]
            maxsum = max(maxsum, current)
            while current <= 0 and left <= right:
                current -= nums[left]
                left += 1
        return maxsum

    def maxSubArray(self, nums: List[int]) -> int:
        '''
        76.21%
        作者：z1m
        动态规划，原地修改数组
        '''
        maxnum = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            maxnum = max(maxnum,nums[i])
        return maxnum
                
# @lc code=end


if __name__ == "__main__":
    S = Solution()
    print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))