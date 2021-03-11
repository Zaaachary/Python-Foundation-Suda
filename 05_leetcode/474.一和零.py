#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from typing import List

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        暴力法  O(n^2)
        '''
        # strs => (0count, 1count)
        for index, binstr in enumerate(strs):
            strs[index] = (binstr.count('0'), binstr.count('1'))
        
        max_subset_size = 0

        for left in range(len(strs)):
            cur_m, cur_n = 0, 0
            for right in range(left, len(strs)):
                cur_m += strs[right][0]
                cur_n += strs[right][1]
                if cur_m <= m and cur_n <=n:
                    max_subset_size = max(max_subset_size, right-left+1)
                else:
                    break
            
        return max_subset_size
        



# @lc code=end

if __name__ == "__main__":
    S = Solution()
    print(S.findMaxForm(["10", "0001", "111001", "1", "0"], m = 5, n = 3))