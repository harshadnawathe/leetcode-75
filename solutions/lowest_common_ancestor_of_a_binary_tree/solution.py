from collections import deque
from typing import Deque, Dict, Optional, Tuple

from commons.tree import TreeNode


class TreeNodeInfo:
    def __init__(self, parent: Optional[TreeNode], depth: int):
        self.parent = parent
        self.depth = depth


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        tree_node_info = self.get_tree_node_info(root)

        while tree_node_info[p].depth > tree_node_info[q].depth:
            parent = tree_node_info[p].parent
            assert parent is not None
            p = parent

        while tree_node_info[q].depth > tree_node_info[p].depth:
            parent = tree_node_info[q].parent
            assert parent is not None
            q = parent

        while p is not q:
            p_parent = tree_node_info[p].parent
            assert p_parent is not None
            p = p_parent

            q_parent = tree_node_info[q].parent
            assert q_parent is not None
            q = q_parent

        return p

    def get_tree_node_info(self, root: TreeNode) -> Dict[TreeNode, TreeNodeInfo]:
        tree_node_info = dict()

        nodes: Deque[Tuple[TreeNode, Optional[TreeNode], int]] = deque(
            [(root, None, 0)]
        )

        while nodes:
            node, parent, depth = nodes.popleft()

            tree_node_info[node] = TreeNodeInfo(parent, depth)

            if node.left is not None:
                nodes.append((node.left, node, depth + 1))

            if node.right is not None:
                nodes.append((node.right, node, depth + 1))

        return tree_node_info
