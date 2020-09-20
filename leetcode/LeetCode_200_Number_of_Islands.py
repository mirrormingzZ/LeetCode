from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        opt = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0

        def dfs(x, y) -> None:
            visited[x][y] = True
            for d in opt:
                nx, ny = x + d[0], y + d[1]
                if -1 < nx < m and -1 < ny < n and not visited[nx][ny] and grid[nx][ny] == "1":
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)
        return res


s = Solution()
res = s.numIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
)
print(res)






