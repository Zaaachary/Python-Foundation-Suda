#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insert_loc = len(nums)
        left, right = 0, insert_loc-1
        while left <= right:
            mid = left + (right - left) // 2
            temp = nums[mid]
            if temp >= target:
                insert_loc = min(insert_loc, mid)
                right = mid -1
            elif temp < target:
                left = mid + 1
        
        return insert_locs
            

# @lc code=end

class Solution_old:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 36ms 91.22%
        for index, num in enumerate(nums):
            if num < target:
                continue
            elif num > target:
                nums.insert(index, target)
                return index
            elif num == target:
                return index
        else:
            # 位置在最尾部
            nums.append(target)
            return len(nums)-1


if __name__ == "__main__":
    test = [1,3,5,6]
    i = 5
    S = Solution()
    print(S.searchInsert(test, i))