from commons.tree import TreeNode
from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        return (
            self.searchBST(root.left, val)
            if val < root.val
            else self.searchBST(root.right, val)
        )
