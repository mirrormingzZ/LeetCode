from typing import List


class Solution:
    opt = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.word_search(board, visited, word, 0, i, j):
                    return True
        return False

    def word_search(self, board, visited, word, index, x, y) -> bool:
        def in_area(m, n) -> bool:
            return 0 <= m < len(board) and 0 <= n < len(board[0])

        # 如果是最后一个元素
        if len(word) - 1 == index:
            return word[index] == board[x][y]
        # 如果当前元素匹配
        if word[index] == board[x][y]:
            visited[x][y] = True
            for op in self.opt:
                n_x = x + op[0]
                n_y = y + op[1]
                if in_area(n_x, n_y) and not visited[n_x][n_y] \
                        and self.word_search(board, visited, word, index + 1, n_x, n_y):
                    return True
            visited[x][y] = False
        return False


class Solution3:
    def __init__(self):
        self.visited = set()

    opt = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if self.word_search(board, word, 0, i, j):
                    return True
        return False

    def word_search(self, board, word, index, x, y) -> bool:
        def in_area(m, n) -> bool:
            return 0 <= m < len(board) and 0 <= n < len(board[0])

        # 如果是最后一个元素
        if len(word) - 1 == index:
            return word[index] == board[x][y]
        # 如果当前元素匹配
        if word[index] == board[x][y]:
            self.visited.add((x, y))
            for a, b in self.opt:
                n_x, n_y = x + a, y + b
                if in_area(n_x, n_y) and (n_x, n_y) not in self.visited and self.word_search(board, word, index + 1,
                                                                                             n_x, n_y):
                    return True
            self.visited.remove((x, y))
        return False


class Solution4:
    opt = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        need = dict()
        for x in word:
            need[x] = word.count(x)

        for i in range(m):
            for j in range(n):
                if board[i][j] in need: need[board[i][j]] -= 1

        if any(map(lambda x: x > 0, need.values())):
            return False

        def word_search(index, x, y) -> bool:
            def in_area(m, n) -> bool:
                return 0 <= m < len(board) and 0 <= n < len(board[0])

            # 如果是最后一个元素
            if len(word) - 1 == index: return word[index] == board[x][y]
            # 如果当前元素匹配
            if word[index] == board[x][y]:
                visited[x][y] = True
                for a, b in self.opt:
                    n_x, n_y = x + a, y + b
                    if in_area(n_x, n_y) and not visited[n_x][n_y] and word_search(index + 1, n_x, n_y):
                        return True
                visited[x][y] = False
            return False

        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if word_search(0, i, j): return True
        return False


s = Solution4()
b = s.exist(
    [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ],
    "SEE")

print(b)
