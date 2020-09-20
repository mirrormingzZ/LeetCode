from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        userd = [False for _ in range(l + 10)]
        cur = []

        def helper(length, idx=0):
            if length == len(cur):
                res.append([*cur])
                return
            for i in range(idx, l):
                if not userd[nums[i]]:
                    cur.append(nums[i])
                    userd[nums[i]] = True
                    helper(length, i + 1)
                    cur.pop()
                    userd[nums[i]] = False

        for x in range(l + 1):
            print("循环插入" + str(x))
            helper(x)
        return res


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(sol, index, arr):
            res.append(sol)
            for i in range(index, len(arr)):
                backtrack(sol + [arr[i]], i + 1, arr)

        backtrack([], 0, nums)
        return res


s = Solution2()
res = s.subsets([1, 2, 3, 4])
print(res)
