#! -*- encoding:utf-8 -*-
"""
@File    :   141.环形链表.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   hash表、快慢指针、链表计数、链表反转、标记val值
"""


#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @lc code=start
class Solution:
    def hasCycle_01(self, head: ListNode) -> bool:
        '''
        使用 list 记录 id 5%
        '''
        id_list = []
        while head:
            if id(head) in id_list:
                return True
            else:
                id_list.append(id(head))
            head = head.next
        else:
            return False

    def hasCycle_02(self, head: ListNode) -> bool:
        # hash
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False

    def hasCycle_03(self, head: ListNode) -> bool:
        '''
        快慢指针 v1  12.92%
        '''
        fast = head
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
            if slow == fast:
                return True
        else:
            return False

    def hasCycle_04(self, head: ListNode) -> bool:
        '''
        快慢指针 v1  44.44%
        使用 bool 标记 slow pointer 走不走
        '''
        sp, fp, si = head, head, False
        while fp:
            if si:
                sp = sp.next
                si = False
            else:
                si = True
            fp = fp.next
            if sp == fp:
                return True
        return False

    def hasCycle_05(self, head: ListNode) -> bool:
        '''
        python 语言特性，给对象设置 mark
        '''
        fp = head
        while fp:
            if hasattr(fp, 'mark'):
                return True
            else:
                fp.mark = True
                fp = fp.next
        else:
            return False
            

        
# @lc code=end

if __name__ == "__main__":
    pass