#! -*- encoding:utf-8 -*-
"""
@File    :   Offer 48 最长不含重复字符的子字符串.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""
#%%
class Solution:
    def lengthOfLongestSubstring_bad(self, s: str) -> int:
        # 暴力法  5%
        if len(s) <= 1:
            return len(s)
        max_len = 1
        for left in range(len(s)):
            right = left + 1
            while len(set(s[left:right])) == right-left:
                max_len = max(max_len, right-left)
                right += 1
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力法  5%
        if len(s) <= 1:
            return len(s)
        max_len = 1
        for left in range(len(s)):
            right = left + 1
            while len(set(s[left:right])) == right-left:
                max_len = max(max_len, right-left)
                right += 1
        return max_len

#%%
if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring('pwwkew'))
# %%
