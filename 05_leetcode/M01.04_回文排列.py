"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。


判断字符串能否重写排列成回文
"""
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 48ms 23.76%  两个及以上字符出现次数为奇数
        ch_dict = Counter(s)        
        odd = 0
        for value in ch_dict.values():
            if value %2 ==1:
                if (odd:=odd+1) > 1:
                    return False
        return True


if __name__ == "__main__":
    S = Solution()
    print(S.canPermutePalindrome("ab"))