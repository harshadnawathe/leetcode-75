from commons.tree import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        nodes = [root]

        max_depth = 0
        while nodes:
            max_depth += 1

            nodes = [
                child for node in nodes for child in (node.left, node.right) if child
            ]

        return max_depth
