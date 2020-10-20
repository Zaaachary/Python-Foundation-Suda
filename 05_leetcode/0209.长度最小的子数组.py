"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 64ms  37.49%用户
        if len(nums) > 1:
            min_len = len(nums)+1
            slow, fast = 0, 0  # slow子串首 fast子串尾巴 初始状态仅一个元素
            nsum = nums[0]
            while slow <= fast:
                if nsum < s:
                    fast += 1
                    if fast < len(nums):
                        nsum += nums[fast]
                    else:
                        # fast已经outofindex
                        break
                elif nsum >= s:
                    min_len = min(min_len, fast-slow+1)
                    nsum -= nums[slow]
                    slow += 1
            if min_len <= len(nums):
                return min_len
            else:
                return 0
        elif sum(nums) >= s:
            return 1
        else:
            # 不存在满足条件的子数组
            return 0
    
    def minSubArrayLen2(self, s:int, nums:List[int]) -> int:
        # 解析  无需判断len(nums)>1  56ms
        slow=0
        min_len=float('inf')
        nsum=0
        
        for fast in range(len(nums)):
            nsum+=nums[fast]
            
            while nsum>=s:
                min_len = min(min_len,fast-slow+1)
                nsum -= nums[slow]
                slow+=1
        
        return min_len if min_len!=float('inf') else 0



if __name__ == "__main__":
    # nums, s = [1,1], 3
    # nums, s = [1,2,3,4,5], 15
    nums, s = [2,3,1,2,4,3], 7
    S = Solution()
    print(S.minSubArrayLen(s, nums))
