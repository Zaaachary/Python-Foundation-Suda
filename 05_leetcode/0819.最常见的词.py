"""
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。
返回出现次数最多，同时不在禁用列表中的单词。
题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。

"""
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 56ms 36%
        word_dict = dict.fromkeys(banned, -1)
        for word in re.finditer(r"[a-zA-Z]+", paragraph):
            word = word.group().lower()
            if word_dict.get(word) == -1:
                # 违禁词
                continue
            else:
                word_dict[word] = word_dict.get(word,0) +1
        return max(word_dict, key=lambda x:word_dict[x])


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    S = Solution()
    print(S.mostCommonWord(paragraph, banned))