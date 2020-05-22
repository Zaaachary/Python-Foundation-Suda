"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

- 如果剩余字符少于 k 个，则将剩余字符全部反转。
- 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for index in range(0, len(s), 2*k):
            s_list[index:index+k] = reversed(s_list[index:index+k])
        return ''.join(s_list)


if __name__ == "__main__":
    S = Solution()
    print(S.reverseStr("abcdefg", 2))