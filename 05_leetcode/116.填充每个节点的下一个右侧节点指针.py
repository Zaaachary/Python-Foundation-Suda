#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
"""
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        # 初始化队列 将第一层节点加入队列中
        Q = deque([root])
        while Q:
            # 记录当前队列大小
            size = len(Q)
            # 遍历这一层的所有节点
            for i in range(size):
                node = Q.popleft()
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return root



# class Solution_old:
#     def connect(self, root: 'Node') -> 'Node':
#         '''
#         92.92% 5.18%
#         层序遍历  （广度优先遍历）  使用end标记结束
#         '''
#         if root is None:
#             return None
#         Q = deque([root, 'end'])
#         prior = None
#         while Q:
#             node = Q.popleft()
#             if node == "end":
#                 # 某层的末尾
#                 prior.next = None
#                 prior = None
#                 if len(Q):  # 队列中仍有节点 则标记末尾
#                     Q.append("end")
#             else:
#                 if prior is not None:
#                     # node 是某层中间的节点
#                     prior.next = node
#                 prior = node
#                 if prior.left:
#                     Q.append(prior.left)
#                     Q.append(prior.right)

#         return root
        
        
        
# @lc code=end

