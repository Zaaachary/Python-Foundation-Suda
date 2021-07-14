#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        86.59%   13.34%
        '''
        fake_head = ListNode(-1)
        fake_head.next = head

        slow = fast = fake_head
        for _ in range(n):
            fast = fast.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        delete = slow.next
        slow.next = delete.next
        del delete
        
        return fake_head.next

# @lc code=end

