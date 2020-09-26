""""
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return '%s %s %s' % (self.val, self.left, self.right)


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node: TreeNode, s: int) -> None:
            if not node:
                return
            cur_val = node.val
            path.append(cur_val)
            if not node.left and not node.right and s == cur_val:
                res.append([*path])
            s -= cur_val
            dfs(node.left, s)
            dfs(node.right, s)
            path.pop()

        dfs(root, sum)
        return res


class Solution2:
    def pathSum(self, root: TreeNode, xsum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = []

        def dfs(node, target):
            if node:
                stack.append(node.val)
            if not node.left and not node.right:
                if sum(stack) == target:
                    tmp = [i for i in stack]
                    res.append(tmp)
                return
            if node.left:
                dfs(node.left, target)
                stack.pop()
            if node.right:
                dfs(node.right, target)
                stack.pop()

        dfs(root, xsum)
        return res


class Solution3:
    def pathSum(self, root: TreeNode, sum_path: int) -> List[List[int]]:
        if not root:
            return []
        stack_node = [([root.val], root)]
        ans = []
        while stack_node:
            cur_sum, cur_node = stack_node.pop()
            if not cur_node.right and not cur_node.left and sum(cur_sum) == sum_path:
                ans.append(cur_sum)
            if cur_node.right:
                stack_node.append(
                    (cur_sum + [cur_node.right.val], cur_node.right))
            if cur_node.left:
                stack_node.append(
                    (cur_sum + [cur_node.left.val], cur_node.left))
        return ans


if __name__ == '__main__':
    r = TreeNode(5)

    r.left = TreeNode(4)
    r.right = TreeNode(8)

    r.left.left = TreeNode(11)

    r.left.left.left = TreeNode(7)
    r.left.left.right = TreeNode(2)

    r.right.left = TreeNode(13)
    r.right.right = TreeNode(4)
    r.right.right.left = TreeNode(5)
    r.right.right.right = TreeNode(1)

    s = Solution3()
    res = s.pathSum(r, 22)
    print(res)
