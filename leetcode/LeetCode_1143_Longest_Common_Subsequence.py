from typing import List
from bisect import bisect_left


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        res = 0

        def helper(t1, t2) -> int:
            if not t1:
                return 0
            if not t2:
                return 0
            if text1[t1] == text2[t2]:
                return 1 + helper(t1[:len(t1) - 1], t2[:len(t2) - 1])
            else:
                return helper(t1[:len(t1) - 1], t2) + helper(t1, t2[:len(t2) - 1])

        res += helper(text1, text2)
        return res


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(i, j):
            # 初始化base case
            if i == -1 or j == -1:
                return 0
            # 状态转移
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(len(text1) - 1, len(text2) - 1)


s = Solution2()
res = s.longestCommonSubsequence("abcde", "ace")
print(res)
