from typing import List, Optional

from commons.tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        nodes = [root] if root else []

        while nodes:
            result.append(nodes[-1].val)

            nodes = [
                child for node in nodes for child in (node.left, node.right) if child
            ]

        return result
