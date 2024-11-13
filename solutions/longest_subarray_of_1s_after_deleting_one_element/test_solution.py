from solutions.longest_subarray_of_1s_after_deleting_one_element.solution import (
    Solution,
)


tests = [
    ("Example 1", {"args": {"nums": [1, 1, 0, 1]}, "expected": 3}),
    ("Example 2", {"args": {"nums": [0, 1, 1, 1, 0, 1, 1, 0, 1]}, "expected": 5}),
    ("Example 3", {"args": {"nums": [1, 1, 1]}, "expected": 2}),
]


def test_longest_subarray_of_1s_after_deleting_one_element(args, expected):
    solution = Solution()

    assert solution.longestSubarray(**args) == expected
