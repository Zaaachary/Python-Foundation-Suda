#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

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

if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLongestSubstring(''))

