from collections import defaultdict
from typing import Optional

from commons.tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_sums[curr_sum - targetSum]

            prefix_sums[curr_sum] += 1
            count += dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1  # Backtrack

            return count

        prefix_sums = defaultdict(int, {0: 1})
        return dfs(root, 0)
