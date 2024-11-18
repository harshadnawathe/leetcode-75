from commons.tree import TreeNode
from typing import DefaultDict, Optional
from collections import defaultdict


class Solution:
    def path_sum(self, node: Optional[TreeNode], curr_sum: int) -> int:
        if node is None:
            return 0

        curr_sum += node.val

        result = self.count[curr_sum - self.target]

        self.count[curr_sum] += 1

        result += self.path_sum(node.left, curr_sum) + self.path_sum(
            node.right, curr_sum
        )

        self.count[curr_sum] -= 1

        return result

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count: DefaultDict[int, int] = defaultdict(int, [(0, 1)])
        self.target = targetSum

        return self.path_sum(root, 0)
