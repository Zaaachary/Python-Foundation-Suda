#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#
def isBadVersion(num):
    if num >= 4:
        return True
    return False

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        找到最小的 bad
        :type n: int
        :rtype: int
        """
        min_bad = n + 1
        start, end = 1, n
        while start <= end:
            mid = end + (start - end)//2  #  其他语言计算防止溢出
            # mid = (start + end)//2
            bad = isBadVersion(mid)
            if bad:
                min_bad = mid if min_bad > mid else min_bad
                end = mid - 1
            else:
                start = mid + 1

        return min_bad
            
        
# @lc code=end

if __name__ == "__main__":
    S = Solution()
    print(S.firstBadVersion(5))

