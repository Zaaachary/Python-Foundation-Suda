"""
你有一个日志数组 logs。每条日志都是以 空格分隔的字串。

对于每条日志，其第一个字为字母与数字混合的 标识符。

- 除标识符之外，所有字均由小写字母组成的，称为 字母日志
- 除标识符之外，所有字均由数字组成的，称为 数字日志

题目所用数据保证每个日志在其标识符后面至少有一个字。

请按下述规则将日志重新排序：

- 所有 字母日志 都排在 数字日志 之前。
- 字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序；
- 数字日志 应该按原来的顺序排列。

返回日志的最终顺序。
"""
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 52ms sort 元组key
        def comput_weight(log):
            tag, content = log.split(' ', 1)
            if content[0].isalpha():
                return (0, content, tag)
            else:
                return (1,)

        logs.sort(key=lambda x:comput_weight(x))
        return logs


if __name__ == "__main__":
    log1 =["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
    S = Solution()
    print(S.reorderLogFiles2(log1))