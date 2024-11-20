from typing import Generator, Optional, Tuple
from commons.tree import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self._level_sums(root), key=lambda x: x[1])[0]

    def _level_sums(self, root: TreeNode) -> Generator[Tuple[int, int], None, None]:
        level, nodes = 1, [root]

        while nodes:
            yield level, sum(node.val for node in nodes)
            level += 1
            nodes = [
                child for node in nodes for child in (node.left, node.right) if child
            ]
