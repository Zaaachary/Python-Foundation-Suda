'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。


[0] [1] [2] [3] [4] [5]



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 哈希表 60ms 84.54%
        visited = {} 
        while head:
            if visited.get(head, False):
                return head
            else:
                visited[head] = True
            head = head.next
        else:
            return

    def detectCycle2(self, head: ListNode) -> ListNode:
        # https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
        fast, slow = head, head  # f = 2s
        while True:
            if not (fast and fast.next): return  # 快指针遇到None
            fast, slow = fast.next.next, slow.next
            if fast == slow: break  # 第一次相遇 f = s + nb; f = 2nb, s = nb
        fast = head
        while fast != slow: # 第二次相遇  s = a + nb  f = a
            fast, slow = fast.next, slow.next
        return fast

    def CreateCycle(self, val: List, pos: int) -> ListNode:
        # 输入val和pos生成一个用于测试的链表
        if len(val) < 1:
            return None

        head, cycle = ListNode('start'), None # 头节点 入环第一个结点
        temp = head
        
        for i, v in enumerate(val):
            temp.next = ListNode(v)
            temp = temp.next
            if i == pos:
                cycle = temp # 当前的temp是入环的第一个结点
        else:
            if cycle:
                temp.next = cycle

        return head


if __name__ == "__main__":
    S = Solution()
    head = S.CreateCycle([i for i in range(5)], 3)
    print(S.detectCycle2(head).val)