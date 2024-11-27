from solutions.maximum_subsequence_score.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"nums1": [1, 3, 3, 2], "nums2": [2, 1, 3, 4], "k": 3},
            "expected": 12,
        },
    ),
    (
        "Example 2",
        {
            "args": {"nums1": [4, 2, 3, 1, 1], "nums2": [7, 5, 10, 9, 6], "k": 1},
            "expected": 30,
        },
    ),
]


def test_maximum_subsequence_score(args, expected):
    solution = Solution()

    assert solution.maxScore(**args) == expected
