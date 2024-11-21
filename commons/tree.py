from typing import Iterable, List, Optional


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TreeNode):
            return NotImplemented
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __hash__(self) -> int:
        return hash((self.val, self.left, self.right))

    def get_node_with_val(self, val: int) -> Optional["TreeNode"]:
        queue: List[TreeNode] = [self]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    @classmethod
    def from_vals(cls, vals: Iterable[Optional[int]]) -> Optional["TreeNode"]:
        vals_iter = iter(vals)
        root_val = next(vals_iter, None)
        if root_val is None:
            return None

        root = cls(root_val)
        queue = [root]

        for val in vals_iter:
            node = queue.pop(0)
            if val is not None:
                node.left = cls(val)
                queue.append(node.left)
            try:
                val = next(vals_iter)
                if val is not None:
                    node.right = cls(val)
                    queue.append(node.right)
            except StopIteration:
                break

        return root
