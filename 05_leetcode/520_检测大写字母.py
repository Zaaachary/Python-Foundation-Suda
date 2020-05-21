"""
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

- 全部字母都是大写，比如"USA"。
- 单词中所有字母都不是大写，比如"leetcode"。
- 如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。

否则，我们定义这个单词没有正确使用大写字母。
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 36ms 85%
        if len(word) <= 1:
            return True
        firstB = True if word[0].isupper() else False
        secendB = True if word[1].isupper() else False
        if not firstB and secendB:
            return False

        for ch in word[2:]:
            if not firstB:
                # 首字母小写
                if ch.isupper():
                    return False
            elif secendB:
                # 第二个字母也大写

                if ch.islower():
                    return False
            else:
                # 第二个字母小写
                if ch.isupper():
                    return False
        else:
            return True
                


if __name__ == "__main__":
    S = Solution()
    test = 'usA'
    print(S.detectCapitalUse(test))