from commons.tree import TreeNode
from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Replace with largest in the left subtree or smallest in the right subtree
            largest = self._largest(root.left)
            root.val = largest.val
            root.left = self.deleteNode(root.left, largest.val)

        return root

    def _largest(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node
