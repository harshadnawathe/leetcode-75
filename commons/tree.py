from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    @classmethod
    def from_vals(cls, vals: Iterable[Optional[int]]) -> Optional["TreeNode"]:
        vals_iter = iter(vals)

        def next_val():
            try:
                val = next(vals_iter)
                return val, False
            except StopIteration:
                return None, True

        root_val, stop = next_val()

        if stop or root_val is None:
            return None

        root = TreeNode(root_val)

        nodes = [root]

        while True:
            node = nodes.pop(0)

            val, stop = next_val()

            if stop:
                break

            if val is not None:
                node.left = TreeNode(val)
                nodes.append(node.left)

            val, stop = next_val()

            if stop:
                break

            if val is not None:
                node.right = TreeNode(val)
                nodes.append(node.right)

        return root
