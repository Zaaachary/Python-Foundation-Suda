#! -*- encoding:utf-8 -*-
"""
@File    :   Offer 56.I 数组中数字出现的次数.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

输入：nums = [3,4,3,3]
输出：4
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        time: 28.47%; memory: 80.97%
        将所有数字的二进制每一位相加，如果某一位能被3整除
        '''
        bits = [0] * 32
        for num in nums:
            bitmask = 1
            for i in range(31, -1, -1):
                if num & bitmask:
                    bits[i] += 1
                bitmask <<= 1
        result = 0
        for i in range(32):
            result = result << 1
            result += bits[i]%3
        return result


if __name__ == "__main__":
    S = Solution()
    print(S.singleNumber([3,4,3,3]))