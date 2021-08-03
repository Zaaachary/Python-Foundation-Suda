#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from typing import List

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        runtime beats 69.26 %
        memory usage beats 31.53 %
        非递减 -> 平方后亦非递减
        双指针 左右往内
        """
        nums = [num**2 for num in nums]
        result = [0] * len(nums)
        left, right = 0, len(nums)-1
        index = right
        while left <= right:
            l, r = nums[left], nums[right]
            if l >= r:
                result[index] = l
                left +=1
            else:
                result[index] = r
                right -=1
            index -= 1

        return result


# @lc code=end

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        time beats 43.59%
        memory beats 98.13%
        非递减 -> 平方后亦非递减
        分负数列表和正数列表，随后归并
        """
        max_neg = -1
        for index, num in enumerate(nums):
            if num <= 0:
                max_neg = index
            nums[index] = num**2

        neg_nums = nums[max_neg::-1] if max_neg!=-1 else []
        pos_nums = nums[max_neg+1:]

        # 归并
        n_index, p_index = 0, 0
        while n_index < len(neg_nums) and p_index < len(pos_nums):
            if neg_nums[n_index] <= pos_nums[p_index]:
                nums[n_index+p_index] = neg_nums[n_index]
                n_index += 1
            else:
                nums[n_index+p_index] = pos_nums[p_index]
                p_index += 1
        else:
            if n_index < len(neg_nums):
                nums[n_index+p_index:] = neg_nums[n_index:]
            else:
                nums[n_index+p_index:] = pos_nums[p_index:]


        return nums


if __name__ == "__main__":
    S = Solution()
    print(S.sortedSquares([-1]))
    print(S.sortedSquares([-2, -1, 0,0,1, 2, 3]))