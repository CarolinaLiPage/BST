class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        row_cnt = len(rooms)

        # Special case handling
        if row_cnt == 0:
            return

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROOM, GATE = (1 << 31) - 1, 0

        col_cnt = len(rooms[0])
        q = collections.deque()

        # Put all GATEs into the queue
        for row in range(row_cnt):
            for col in range(col_cnt):
                if rooms[row][col] == GATE:
                    q.append((row, col))

        while q:
            curr_row, curr_col = q.popleft()

            # Check neighbors in 4 directions
            for dr, dc in DIRECTIONS:
                next_row = curr_row + dr
                next_col = curr_col + dc

                # If the next room is within the boundary and is a ROOM
                if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt and rooms[next_row][next_col] == ROOM:
                    # Update the distance to the nearest gate
                    rooms[next_row][next_col] = rooms[curr_row][curr_col] + 1
                    # Put the next room into the queue
                    q.append((next_row, next_col))
