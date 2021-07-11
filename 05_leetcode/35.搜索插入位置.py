#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

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

