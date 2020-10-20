#! -*- encoding:utf-8 -*-
"""
@File    :   5_最长回文子串.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   Leetcode

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        naive dp; 8728ms 5%; 22.2MB, 5.23%; 遍历了所有可能的结果
        '''
        longest = ''
        dp_matrix = [[True for _ in range(len(s))] for start in range(len(s))]                
        for end in range(0, len(s)):
            for start in range(0, end+1):
                if start == end:
                    if len(longest) ==0: longest = s[start]
                elif s[start] == s[end] and start + 1 <= end and dp_matrix[start+1][end-1]:
                    if end-start+1 > len(longest):
                        longest = s[start:end+1]
                else:
                    dp_matrix[start][end] = False
        return longest
        
    def longestPalindrome2(self, s: str) -> str:
        '''
        作者：skay2002  来源：力扣（LeetCode）
        '''
        if not s: return ""
        length = len(s)
        if length == 1 or s == s[::-1]: return s
        max_len,start = 1,0
        for i in range(1, length):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]


if __name__ == "__main__":
    S = Solution()
    print(S.longestPalindrome('babad'))
    print(S.longestPalindrome('cdd'))