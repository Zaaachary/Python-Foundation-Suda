#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

from typing import List

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        双指针 99.84% 5.01%
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

# @lc code=end

class Solution_1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        # runtime 99.11; memory 25.26%
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        last_not_zero = 0
        for num in nums:
            if num == 0:
                zero_count += 0
            elif last_not_zero != -1:
                nums[last_not_zero] = num
                last_not_zero += 1
        for index in range(last_not_zero, len(nums)):
            nums[index] = 0

if __name__ == "__main__":
    S = Solution()
    l = [1,2,3,4,0]
    S.moveZeroes(l)
    print(l)
