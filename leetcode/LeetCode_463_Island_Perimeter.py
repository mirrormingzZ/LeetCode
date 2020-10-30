"""
463.
岛屿的周长
给定一个包含0和1的二维网格地图，其中1表示陆地0表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为1的正方形。网格为长方形，且宽度和高度均不超过100 。计算这个岛屿的周长。

示例:

输入:
[[0, 1, 0, 0],
 [1, 1, 1, 0],
 [0, 1, 0, 0],
 [1, 1, 0, 0]]

输出: 16
"""
from functools import reduce
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        c = ((-1, 0), (0, -1), (1, 0), (0, 1))
        len_x, len_y = len(grid[0]), len(grid)

        def calc(x, y):
            l = 4
            for m, n in c:
                n_x, n_y = x + m, y + n
                if 0 <= n_x < len_y and 0 <= n_y < len_x:
                    l -= grid[n_x][n_y]
            return l

        for i in range(len_y):
            for j in range(len_x):
                if grid[i][j]:
                    res += calc(i, j)
        return res


s = Solution()
result = s.islandPerimeter([[0, 1, 0, 0],
                            [1, 1, 1, 0],
                            [0, 1, 0, 0],
                            [1, 1, 0, 0]])

print(result)
