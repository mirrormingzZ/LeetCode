"""
538. 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return '%s %s %s' % (self.val, self.left, self.right)


class Solution:
    total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if node:
                # 先遍历到最右节点
                dfs(node.right)
                # 累加赋值
                self.total += node.val
                node.val = self.total
                # 最后遍历左节点
                dfs(node.left)

        dfs(root)
        return root


r = TreeNode(5)
r.left = TreeNode(3)
r.right = TreeNode(13)
r.left.left = TreeNode(1)
r.left.right = TreeNode(4)
r.right.left = TreeNode(10)
r.right.right = TreeNode(15)

s = Solution()
res = s.convertBST(r)
print(res)
