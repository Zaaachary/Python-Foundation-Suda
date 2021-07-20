#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        90.54%  53.42%
        滑动窗口（双指针）  滑窗内为不重复的子串，利用集合来判断是否重复
        '''
        max_len = cur_len = 0
        left = right =0

        temp_set = set()
        while right < len(s):
            while left < right and s[right] in temp_set:
                temp_set.remove(s[left])
                cur_len -=1
                left += 1
            temp_set.add(s[right])
            cur_len += 1
            right += 1

            max_len = max(max_len, cur_len)

        return max_len

# @lc code=end

class Solution_old:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口 72ms 77.35%
        if len(s) == 0:
            return 0
        ans = f = 0
        for r in range(0, len(s)):
            if s[r] not in s[f:r]:
                ans = max(ans, r-f+1)
            else:
                while s[r] in s[f:r]:
                    f += 1
        # print(s[f:r+1])
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring(''))

