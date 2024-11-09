from solutions.longest_subarray_of_1s_after_deleting_one_element.solution import (
    Solution,
)


def test_longest_subarray_of_1s_after_deleting_one_element():
    solution = Solution()

    assert solution.longestSubarray([1, 1, 0, 1]) == 3
    assert solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert solution.longestSubarray([1, 1, 1]) == 2
