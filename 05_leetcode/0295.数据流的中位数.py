#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
# import bisect
# class MedianFinder:
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.num_list = []

#     def addNum1(self, num: int) -> None:
#         # sort()   11.33%
#         bisect.bisect(self.num_list, num)

#     def addNum2(self, num: int) -> None:
#         # binsearch insert  11.43%
#         self.num_list.append(num)
#         self.num_list.sort()

#     def findMedian(self) -> float:
#         d, m = divmod(len(self.num_list), 2)
#         if m: # odd
#             return self.num_list[d]
#         else: # even
#             return (self.num_list[d] + self.num_list[d-1])/2


import heapq
# pushpop
# push   pop
class MedianFinder:
    
    def __init__(self):
        ''' 79%
        initialize your data structure here.   作者：z1m
        我们将中位数左边的数保存在大顶堆中，右边的数保存在小顶堆中。这样我们可以在 {\mathcal{O}}(1)O(1) 时间内得到中位数。

        注意：Python 中没有大顶堆，只能将值取负保存在小顶堆来模拟。为了方便理解，将堆用优先队列表示。
        '''
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 堆一样大则加入大堆再从大堆中把最大的放到小堆中
        # 堆不一样大（小堆大于大堆），将元素放入小堆后再将最小的元素放入大堆
        if len(self.max_heap) == len(self.min_heap):# 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]




if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

