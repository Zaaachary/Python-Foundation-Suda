#! -*- encoding:utf-8 -*-
"""
@File    :   Offer 56.I 数组中数字出现的次数.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
"""
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        '''
        异或做法   56ms,  77.83%
        '''     
        if len(nums) < 2:
            return
        
        eor = 0
        for num in nums:
            eor ^= num

        # find first bit is 1
        firstBitis1 = 0
        while eor & 1 == 0:
            eor >>= 1
            firstBitis1 += 1
        
        judgegroup = lambda x, n: (x >> n) & 1
        r1, r2 = 0, 0
        for num in nums:
            if judgegroup(num, firstBitis1):
                r1 ^= num
            else:
                r2 ^= num
        
        return r1, r2
        

    def singleNumbers_hash(self, nums: List[int]) -> List[int]:
        '''
        哈希表 + 删除  70+ms
        '''
        n_dict = dict()
        for num in nums:
            n_dict[num] = n_dict.get(num, 0) + 1
            if n_dict[num] == 2:
                del n_dict[num]
        return list(n_dict.keys())

if __name__ == "__main__":
    S = Solution()
    print(S.singleNumbers([1, 2, 5, 2]))