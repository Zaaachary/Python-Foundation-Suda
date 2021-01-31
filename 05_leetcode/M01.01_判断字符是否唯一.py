"""
实现一个算法确定一个字符串s的所有字符是否全都不同
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        # 44ms
        ch_dict = {}
        for ch in astr:
            if ch in ch_dict:
                return False
            else:
                ch_dict[ch] = 1
        else:
            return True

    def isUnique2(self, astr: str) -> bool:
        # 40ms 位法
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')     # 当前字母的偏移
            if (mark & (1 << move_bit)) != 0:   # mark 和此字符串 与
                return False                    # 不为零则表示有字幕出现两次
            else:
                mark |= (1 << move_bit)         # 将当前字母添加到 mark
        return True


if __name__ == "__main__":
    # test = "leetcode"
    test = "let"
    s = Solution()
    print(s.isUnique(test))
