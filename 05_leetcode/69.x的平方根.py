"""
实现 int sqrt(int x)函数
计算并返回x的平方根，其中x是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # 超时 应该换二分法
        half = x//2
        for i in range(1, half+1):
            if i ** 2 <= x < (i+1)**2:
                return i
        else:
            return x

    def mySqrt2(self, x):
        # 44ms 80%
        return int(x**(1/2))

    def mySqrt3(self, x):
        # 60ms 32%  二分法
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2
            square = mid **2
            if square <= x <(mid+1)**2:
                return mid
            elif square > x:
                end = mid -1
            else:
                start = mid + 1
         

if __name__ == "__main__":
    S = Solution()
    for i in range(0, 38):
        print(S.mySqrt3(i))