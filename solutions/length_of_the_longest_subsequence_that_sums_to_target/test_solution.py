from solutions.length_of_the_longest_subsequence_that_sums_to_target.solution import (
    Solution,
)

tests = [
    ("Example 1", {"args": {"nums": [1, 2, 3, 4, 5], "target": 9}, "expected": 3}),
    ("Example 2", {"args": {"nums": [4, 1, 3, 2, 1, 5], "target": 7}, "expected": 4}),
    ("Example 3", {"args": {"nums": [1, 1, 5, 4, 5], "target": 3}, "expected": -1}),
]


def test_length_of_the_longest_subsequence_that_sums_to_target(args, expected):
    solution = Solution()

    assert solution.lengthOfLongestSubsequence(**args) == expected
