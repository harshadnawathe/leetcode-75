from collections import deque
from typing import Deque, List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        maze[entrance[0]][entrance[1]] = "+"
        locations: Deque[List[int]] = deque([entrance])

        distance = 0
        while locations:
            for _ in range(len(locations)):
                [row, col] = locations.popleft()

                if distance > 0 and (
                    row == 0
                    or row == len(maze) - 1
                    or col == 0
                    or col == len(maze[0]) - 1
                ):
                    return distance

                if row + 1 < len(maze) and maze[row + 1][col] == ".":
                    locations.append([row + 1, col])
                    maze[row + 1][col] = "+"
                if row - 1 >= 0 and maze[row - 1][col] == ".":
                    locations.append([row - 1, col])
                    maze[row - 1][col] = "+"
                if col + 1 < len(maze[0]) and maze[row][col + 1] == ".":
                    locations.append([row, col + 1])
                    maze[row][col + 1] = "+"
                if col - 1 >= 0 and maze[row][col - 1] == ".":
                    locations.append([row, col - 1])
                    maze[row][col - 1] = "+"

            distance += 1

        return -1
