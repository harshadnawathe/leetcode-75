from itertools import starmap, zip_longest
from operator import eq
from typing import Optional

from commons.tree import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return all(starmap(eq, zip_longest(self.leaves(root1), self.leaves(root2))))

    def leaves(self, root: Optional[TreeNode]):
        if not root:
            return

        nodes = [root]
        while nodes:
            node = nodes.pop()

            nodes.extend(child for child in (node.left, node.right) if child)

            if not (node.left or node.right):
                yield node.val
