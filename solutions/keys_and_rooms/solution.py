from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def visit(room: int):
            if visited[room]:
                return

            visited[room] = True

            for next_room in rooms[room]:
                visit(next_room)

        visit(0)

        return all(visited)
