#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    # def middleNode(self, head: ListNode) -> ListNode:
    #     '''
    #     50% 15.1%
    #     '''
    #     slow = fast = head
    #     count = 0
    #     while fast.next is not None:
    #         fast = fast.next
    #         count += 1
    #         if count == 2:
    #             count = 0
    #             slow = slow.next
    #     else:
    #         if count == 1:
    #             slow = slow.next


    #     return slow

    def middleNode(self, head: ListNode) -> ListNode:
        '''
        88.4% 5.17%
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
# @lc code=end

