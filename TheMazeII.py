from typing import List
import collections


class Solution:
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        mark = [[-1 for k in range(4)] for i in range(m)]
        mark[start[0]][start[1]] = [0] * 4
        q = collections.deque([(start[0], start[1], i) for i in range(4)])

        while q:
            x, y, d = q.popleft()
            xx, yy = x + dx[d], y + dy[d]
            if xx >= 0 and xx < m and yy >= 0 and yy < n and maze[xx][yy] == 0:
                if mark[xx][yy][d] < 0:
                    mark[xx][yy][d] = mark[x][y][d] + 1
                    q.append((xx, yy, d))
            else:
                if x == destination[0] and y == destination[1]:
                    return mark[x][y][d]
                for i in range(4):
                    if mark[x][y][i] < 0:
                        mark[x][y][i] = mark[x][y][d] + 1
                        q.appendleft((x, y, i))
        return -1
