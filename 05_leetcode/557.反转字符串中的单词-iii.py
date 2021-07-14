#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        使用堆栈  15.95% 8.21%
        "Let's take LeetCode contest"
        "s'teL ekat edoCteeL tsetnoc"
        '''
        result = [' '] * len(s)
        stack = []
        end = len(s) - 1
        while end >= 0:
            if s[end] != ' ':
                stack.append(s[end])
                end -= 1
            else:
                result[end+1:end+1+len(stack)] = stack
                stack.clear()
                end -= 1
        else:
            if len(stack) > 0:
                result[:len(stack)] = stack

        return ''.join(result)



# @lc code=end

class Solution_py:
    def reverseWords(self, s: str) -> str:
        '''
        76.55% 82.21%
        '''
        s_list = s.split(' ')
        for index, string in enumerate(s_list):
            s_list[index] = ''.join(list(reversed(string)))
        return ' '.join(s_list)


if __name__ == "__main__":
    S = Solution()
    print(S.reverseWords('just have a test'))