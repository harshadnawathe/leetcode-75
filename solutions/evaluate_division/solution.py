from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = self._build_graph(equations, values)

        visited: Set[str] = set()

        def dfs(curr: str, end: str, product_so_far: float = 1.0) -> float:
            if curr == end:
                return product_so_far

            try:
                visited.add(curr)

                for neighbour, value in graph[curr]:
                    if neighbour in visited:
                        continue
                    ans = dfs(neighbour, end, product_so_far * value)
                    if ans != -1:
                        return ans
            finally:
                visited.remove(curr)

            return -1

        answers: List[float] = []

        for [A, B] in queries:
            if (A not in graph) or (B not in graph):
                answers.append(-1)
            else:
                answers.append(dfs(A, B))

        return answers

    def _build_graph(
        self, equations: List[List[str]], values: List[float]
    ) -> Dict[str, List[Tuple[str, float]]]:
        graph: Dict[str, List[Tuple[str, float]]] = defaultdict(list)

        for [A, B], value in zip(equations, values):
            graph[A].append((B, value))
            graph[B].append((A, 1 / value))

        return graph
