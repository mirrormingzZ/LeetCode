# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        r = []
        r.append()

        if not root.left and not root.right:
            return [str(root.val)]

        return [str(root.val) + "->" + s for s in (self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right))]

    def lowestCommonAncestor(self, root, p, q):
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        my_res = []
        if not nums:
            return my_res

        my_used = [False for _ in range(len(nums))]

        def helper(arr: List[int], index: int, temp: List, used: [], res: []):
            if index == len(arr):
                my_res.append([i for i in temp])
                return
            for i in range(0, len(arr)):
                if used[i]:
                    continue
                temp.append(arr[i])
                used[i] = True
                helper(arr, index + 1, temp, used, res)
                used[i] = False
                temp.pop()

        helper(nums, 0, [], my_used, my_res)
        return my_res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()


