from commons.tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0

        stack = [(root, root.val)]

        while stack:
            node, max_so_far = stack.pop()

            if max_so_far <= node.val:
                good_node_count += 1
                max_so_far = node.val

            stack.extend(
                (child, max_so_far) for child in (node.left, node.right) if child
            )

        return good_node_count
