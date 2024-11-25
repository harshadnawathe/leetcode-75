from typing import List, Tuple


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = self._build_graph(n, connections)

        count_reordered = 0

        def dfs(node: int, parent: int = -1):
            nonlocal count_reordered

            for neighbour, need_reorder in graph[node]:
                if neighbour != parent:
                    count_reordered += need_reorder
                    dfs(neighbour, node)

        dfs(0)

        return count_reordered

    def _build_graph(
        self, n: int, connections: List[List[int]]
    ) -> List[List[Tuple[int, bool]]]:
        graph = [[] for _ in range(n)]

        for src, dst in connections:
            graph[src].append((dst, True))  # Need reorder as road is present
            graph[dst].append((src, False))  # No reorder

        return graph
