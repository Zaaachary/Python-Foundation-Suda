# 法2 环状替换；法3 数组翻转
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

from typing import List

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        双指针数组翻转 runtime 95.03% memory usage 46.12%
        Do not return anything, modify nums in-place instead.
        """
        move = k % len(nums)
        nums.reverse()
        # nums[move:] = reversed(nums[move:])
        # nums[:move] = reversed(nums[:move])
        left, right = move, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1

        left, right = 0, move-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1


# @lc code=end

class Solution_1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        超时
        Do not return anything, modify nums in-place instead.
        """
        move = k % len(nums)
        for _ in range(move):
            end = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = end

class Solution_1_plus:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        使用辅助数组
        runtime 99.46% memory usage 35.85%
        Do not return anything, modify nums in-place instead.
        """
        move = k % len(nums)
        end = nums[len(nums)-move:]

        nums[move:] = nums[:len(nums)-move]
        nums[:move] = end


if __name__ == "__main__":
    S = Solution()
    l = [1,2,3,4]
    S.rotate(l, 2)
    print(l)