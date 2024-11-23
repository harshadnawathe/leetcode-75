from collections import defaultdict
from typing import DefaultDict, List, Tuple


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = self._adjacency_list(connections)

        count_reordered = 0

        def dfs(node: int, parent: int = -1):
            nonlocal count_reordered

            for neighbour, need_reorder in graph[node]:
                if neighbour != parent:
                    count_reordered += need_reorder
                    dfs(neighbour, node)

        dfs(0)

        return count_reordered

    def _adjacency_list(
        self, connections: List[List[int]]
    ) -> DefaultDict[int, List[Tuple[int, bool]]]:
        graph: DefaultDict[int, List[Tuple[int, bool]]] = defaultdict(list)

        for src, dst in connections:
            graph[src].append(
                (dst, True)
            )  # As the road is present - we may need to reorder it
            graph[dst].append(
                (src, False)
            )  # As the road is present - no need to reorder it

        return graph
