#! -*- encoding:utf-8 -*-
"""
@File    :   Offer 59 - II. 队列的最大值.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：
"""

class MaxQueue:
    # 284ms 66% 8.49%
    def __init__(self):
        self.Queue = []
        self.max = None
        self.len = 0

    def max_value(self) -> int:
        if self.len == 0:
            return -1
        else:
            return self.max

    def push_back(self, value: int) -> None:
        self.Queue.append(value)
        self.len += 1
        if not self.max:
            self.max = value
        else:
            self.max = max(self.max, value)

    def pop_front(self) -> int:
        if self.len == 0:
            return -1
        
        temp = self.Queue.pop(0)
        self.len -=1
        
        if self.len == 0:
            self.max = None
        elif temp == self.max:
            self.max = max(self.Queue)
        return temp


import queue
class MaxQueue2:
    """
    妙啊 但是怎么是  24.67%
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-ii-dui-lie-de-zui-da-zhi-by-leetcod/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


# if __name__ == "__main__":
    # Your MaxQueue object will be instantiated and called as such:
    # obj = MaxQueue()
    # param_1 = obj.max_value()
    # obj.push_back(value)
    # param_3 = obj.pop_front()