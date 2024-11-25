from collections import defaultdict
from typing import List, Dict, Tuple


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = self._build_graph(equations, values)

        def dfs(curr: str, target: str, visited: set, product: float) -> float:
            if curr == target:
                return product
            visited.add(curr)

            for neighbor, value in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited, product * value)
                    if result != -1:
                        return result

            return -1

        results = []
        for A, B in queries:
            if A not in graph or B not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(A, B, set(), 1.0))

        return results

    def _build_graph(
        self, equations: List[List[str]], values: List[float]
    ) -> Dict[str, List[Tuple[str, float]]]:
        graph = defaultdict(list)
        for (A, B), value in zip(equations, values):
            graph[A].append((B, value))
            graph[B].append((A, 1 / value))
        return graph
