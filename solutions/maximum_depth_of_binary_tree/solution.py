from commons.tree import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        nodes = [root] if root is not None else []

        while nodes:
            max_depth += 1

            for _ in range(len(nodes)):
                node = nodes.pop(0)

                if node.left is not None:
                    nodes.append(node.left)

                if node.right is not None:
                    nodes.append(node.right)

        return max_depth
