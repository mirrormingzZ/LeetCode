from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        cur = []
        res = []
        used = [False for _ in range(10)]

        def helper(idx=1):
            if len(cur) == k and sum(cur) == n:
                res.append(cur[:])
                return
            for i in range(idx, 10):
                if not used[i]:
                    used[i] = True
                    cur.append(i)
                    helper(idx + 1)
                    cur.pop()
                    used[i] = False

        helper()
        return res


s = Solution()
res = s.combinationSum3(3, 9)
print(res)
