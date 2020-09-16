"""
给定一个二叉树返回它的中序遍历
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归解法
        result = []
        if not root:
            return result
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result


    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # 非递归解法
        stack, result = [], []

        # 初始化 root及其左链入栈
        while root != None:
            stack.append(root)
            root = root.left
        
        # 迭代遍历
        while len(stack)>0:
            # 栈非空即未完成遍历
            root = stack.pop()
            result.append(root.val)
            # root右孩子right 其right其左链入栈
            root = root.right
            while root != None:
                stack.append(root)
                root = root.left       
             
        return result


if __name__ == "__main__":
