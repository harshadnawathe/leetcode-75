from typing import Optional
from commons.tree import TreeNode
from itertools import zip_longest, starmap
from operator import eq


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return all(starmap(eq, zip_longest(self.leaves(root1), self.leaves(root2))))

    def leaves(self, root: Optional[TreeNode]):
        nodes = [root] if root is not None else []

        while nodes:
            node = nodes.pop()

            if node.left is not None:
                nodes.append(node.left)

            if node.right is not None:
                nodes.append(node.right)

            if node.left is None and node.right is None:
                yield node.val
