from typing import Optional
from commons.tree import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        self.max_zig_zag_len(root, 0, True)
        self.max_zig_zag_len(root, 0, False)

        return self.result

    def max_zig_zag_len(self, node: Optional[TreeNode], zig_zag_len, go_left):
        if node is None:
            return

        self.result = max(self.result, zig_zag_len)

        if go_left:
            self.max_zig_zag_len(node.left, zig_zag_len + 1, False)
            self.max_zig_zag_len(node.right, 1, True)
        else:
            self.max_zig_zag_len(node.left, 1, False)
            self.max_zig_zag_len(node.right, zig_zag_len + 1, True)
