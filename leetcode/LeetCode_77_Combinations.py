from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 0 or k > n or k < 0:
            return [[]]
        res = []

        def helper(n: int, k: int, index: int, arr: [], res: []):
            if k == len(arr):
                res.append([i for i in arr])
                return
            for i in range(index, n + 1):
                arr.append(i)
                helper(n, k, i + 1, arr, res)
                arr.pop()

        helper(n, k, 1, [], res)
        return res


s = Solution()
res = s.combine(4, 2)
print(res)
