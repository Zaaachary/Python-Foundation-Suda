#
# @lc app=leetcode.cn id=567 lang=python3
#

# https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-7k7u/
# [567] 字符串的排列
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        滑窗#1  21.38%  5.85%
        '''
        if len(s1) > len(s2):
            return False
        count_dict = Counter(s1)

        left = 0
        while left <= len(s2) - len(s1):
            count_dict2 = Counter(s2[left:left+len(s1)])
            for key in count_dict.keys():
                if count_dict[key] != count_dict2[key]:
                    break
            else:
                # 无 break 正常运行，说明匹配
                return True
            left += 1
        else:
            return False




# @lc code=end

if __name__ == "__main__":
    S = Solution()
    print(S.checkInclusion('ab', 'eidbaoo'))