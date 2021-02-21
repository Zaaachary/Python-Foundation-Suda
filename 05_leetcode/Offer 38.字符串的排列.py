#! -*- encoding:utf-8 -*-
"""
@File    :   Offer38.字符串的排列.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

输入一个字符串，打印出该字符串中字符的所有排列。
 
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
"""
from typing import List
import itertools 

class Solution:
    def permutation(self, s: str) -> List[str]:
        # 97%
        return list(set([''.join(item) for item in itertools.permutations(s)]))

    def permutation2(self, s: str) -> List[str]:
        list_s, res = list(s), []
        def DFS(current_len):
            # 目前已经确定了 current_len 之前的字符
            nonlocal res, list_s
            if current_len == len(list_s) - 1:
                res.append(''.join(list_s))
                return 
            temp_dict = set()
            # 将 current_len 与
            for i in range(current_len, len(list_s)):
                # 重复则剪枝
                if list_s[i] in temp_dict: continue
                temp_dict.add(list_s[i])
                # 交换，将 list_s[i] 固定在 current_len 的位置
                list_s[i], list_s[current_len] = list_s[current_len], list_s[i]
                DFS(current_len + 1)                
                list_s[i], list_s[current_len] = list_s[current_len], list_s[i]   # 回溯

        DFS(0)
        return res
        

if __name__ == "__main__":
    S = Solution()
    print(S.permutation2('abc'))