from commons.tree import TreeNode
from math import inf


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0

        nodes = [(root, -inf)] if root is not None else []

        while nodes:
            node, max_so_far = nodes.pop()

            if max_so_far <= node.val:
                max_so_far = node.val
                good_node_count += 1

            if node.left is not None:
                nodes.append((node.left, max_so_far))

            if node.right is not None:
                nodes.append((node.right, max_so_far))

        return good_node_count
