from collections import deque, namedtuple
from typing import Deque, Dict, Optional, Tuple

from commons.tree import TreeNode

TreeNodeInfo = namedtuple("TreeNodeInfo", ["parent", "depth"])


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        tree_info = self._build_tree_info(root)

        # Bring p and q to the same depth
        while tree_info[p].depth > tree_info[q].depth:
            p = tree_info[p].parent
        while tree_info[q].depth > tree_info[p].depth:
            q = tree_info[q].parent

        # Find the common ancestor
        while p != q:
            p, q = tree_info[p].parent, tree_info[q].parent

        return p

    def _build_tree_info(self, root: "TreeNode") -> Dict["TreeNode", TreeNodeInfo]:
        tree_info = {}
        queue: Deque[Tuple[TreeNode, Optional[TreeNode], int]] = deque(
            [(root, None, 0)]
        )

        while queue:
            node, parent, depth = queue.popleft()
            tree_info[node] = TreeNodeInfo(parent, depth)

            queue.extend(
                (child, node, depth + 1) for child in (node.left, node.right) if child
            )

        return tree_info
