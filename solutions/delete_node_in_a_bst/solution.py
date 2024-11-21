from commons.tree import TreeNode
from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key == root.val:
            if root.left:
                largest = self._largest(root.left)
                root.val, largest.val = largest.val, root.val
                root.left = self.deleteNode(root.left, key)
            elif root.right:
                smallest = self._smallest(root.right)
                root.val, smallest.val = smallest.val, root.val
                root.right = self.deleteNode(root.right, key)
            else:
                root = None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

    def _smallest(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def _largest(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node
