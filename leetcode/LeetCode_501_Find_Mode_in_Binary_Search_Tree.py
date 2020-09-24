"""
501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        most = 0
        last = None
        cnt = 0

        def inorder(node):
            if not node:
                return

            nonlocal ans, most, last, cnt

            inorder(node.left)

            # 如果当前值和上一个值相等，更新数量
            cnt = 1 if node.val != last else cnt + 1

            # 如果存在和最大值个数相同的，存入结果集
            if cnt == most:
                ans.append(node.val)

            # 记录最大值，如果有超过最大值的，直接更新最大值数组为当前数字
            elif cnt > most:
                most = cnt
                ans = [node.val]
            last = node.val

            inorder(node.right)

        inorder(root)
        return ans


"""
	     6
	    / \
	   4   6
	  / \   \
	 2   4   7
"""

r = TreeNode(6)
r.left = TreeNode(4)
r.right = TreeNode(6)
r.left.left = TreeNode(2)
r.left.right = TreeNode(4)
r.right.right = TreeNode(7)
s = Solution()
res = s.findMode(r)
print(res)
