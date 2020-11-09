"""
链接：https://leetcode-cn.com/problems/longest-mountain-in-array

我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # flag 记录状态，0 平滑状态，1 上升状态，2 下降状态
        res, start, flag = 0, 0, 0

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if flag != 1:
                    start = i - 1
                flag = 1
            elif A[i] < A[i - 1] and flag != 0:
                flag, res = 2, max(res, i - start + 1)
            else:
                flag, start = 0, i
        return res


s = Solution()
r = s.longestMountain([2, 1, 4, 7, 3, 2, 5])
print(r)
