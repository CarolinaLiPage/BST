# 常量 (constant)
class GridType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

class Solution:
    # 不出界的空地
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return grid[x][y] == GridType.EMPTY

    # 以房子为起点，遍历所有空地，计算得房子到所有空地的最短路径
    def bfs(self, grid, i, j, distance_sum, reachable_count):
        distance = {(i, j): 0}
        queue = collections.deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            # 编写置，矩阵中游走的小偏移
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                adj_x, adj_y = x + dx, y + dy
                if not self.is_valid(adj_x, adj_y, grid):
                    continue
                # 如果这个空地还没有被找到达过（不重复找到达的BFS），则入队
                if (adj_x, adj_y) not in distance:
                    queue.append((adj_x, adj_y))
                    distance[(adj_x, adj_y)] = distance[(x, y)] + 1
                    # 更新所有房子到该空地的距离总和
                    distance_sum[(adj_x, adj_y)] = distance_sum.get((adj_x, adj_y), 0) + \
                                                    distance[(adj_x, adj_y)]
                    # 更新可以达到该空地的房子的数量
                    reachable_count[(adj_x, adj_y)] = reachable_count.get((adj_x, adj_y), 0) + 1

    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        # 空地 => 到所有房子的距离之和
        distance_sum = {}
        # 空地 => 可以达到的房子数量
        reachable_count = {}
        houses = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.HOUSE:
                    self.bfs(grid, i, j, distance_sum, reachable_count)
                    houses += 1

        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                # 如果某个空地不能被所有房子到达，则不适合建邮局
                if (i, j) not in reachable_count or \
                        reachable_count[(i, j)] != houses:
                    continue
                min_dist = min(min_dist, distance_sum[(i, j)])
        return min_dist if min_dist != float('inf') else -1