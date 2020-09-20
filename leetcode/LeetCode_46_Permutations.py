class Solution:
    def permute(self, nums):
        visited = [False for _ in nums]
        cur = []
        res = []

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append([i for i in cur])
            for i in range(0, n):
                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    backtrack(first + 1)
                    visited[i] = False
                    cur.pop()

        n = len(nums)
        backtrack()
        return res


s = Solution()
res = s.permute([1, 2, 3])
print(res)
