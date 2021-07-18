#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 99.88%  5.01% 
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        elif root1:
            return root1
        elif root2:
            return root2
# @lc code=end

    # def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    #     if not t1:
    #         return t2
    #     if not t2:
    #         return t1
        
    #     merged = TreeNode(t1.val + t2.val)
    #     merged.left = self.mergeTrees(t1.left, t2.left)
    #     merged.right = self.mergeTrees(t1.right, t2.right)
    #     return merged