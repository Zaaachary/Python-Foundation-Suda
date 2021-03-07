#! -*- encoding:utf-8 -*-
"""
@File    :   JZOF.03.数组中重复的数字.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

"""
from typing import List
from collections import Counter

class Solution:
    def findRepeatNumber01(self, nums: List[int]) -> int:
        '''排序后遍历，寻找相邻且相同  24%'''
        nums.sort()
        priv = nums[0]
        for i in range(1, len(nums)):
            if priv == nums[i]:
                return priv
            else:
                priv = nums[i]

    def findRepeatNumber02(self, nums: List[int]) -> int:
        '''哈希表法，此处调用标准库   35%'''
        c_d = Counter(nums)
        return c_d.most_common(1)[0][0]

    def findRepeatNumber03(self, nums: List[int]) -> int:
        '''哈希表法   50%'''
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            if num_count[num] == 2:
                return num

    def findRepeatNumber04(self, nums: List[int]) -> int:
        '''
        利用 n 个数字都在0~n-1范围
        目标是遍历的过程中交换，使得每个数字m在m位上
        若m位已经有一个数字m了，则当前的m为一个重复数字
        66.71%
        '''
        index = 0
        while index < len(nums):
            curnum = nums[index]
            if index == curnum:
                index += 1
                continue
            elif nums[curnum] == curnum:
                return curnum
            else:
                nums[curnum], nums[index] = nums[index], nums[curnum]
        else:
            return -1

    def findRepeatNumber(self, nums: List[int]) -> int:
        '''
        思路同上，效率更高
        作者：Dean-98543  96.77%
        '''
        for idx in range(len(nums)):
            while nums[idx] != idx:             # 发现这个坑的萝卜不是自己家的
                if nums[idx]==nums[nums[idx]]:  # 如果发现这个萝卜它家里有了和它一样的萝卜
                    return nums[idx]            # 说明这个萝卜是双胞胎，将它上交国家
                else:
                    # 把这个萝卜送回它家去，然后把它家里的萝卜拿回来
                    nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]




if __name__ == "__main__":
    S = Solution()
    T = [2, 3, 1, 0, 2, 5, 3]
    print(S.findRepeatNumber(T))