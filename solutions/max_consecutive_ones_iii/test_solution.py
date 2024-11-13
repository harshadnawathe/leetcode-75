from solutions.max_consecutive_ones_iii.solution import Solution

tests = [
    (
        "Example 1",
        {"args": {"nums": [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], "k": 2}, "expected": 6},
    ),
    (
        "Example 2",
        {
            "args": {
                "nums": [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                "k": 3,
            },
            "expected": 10,
        },
    ),
    (
        "Example 3",
        {"args": {"nums": [1, 1, 1, 0, 0, 0, 0, 0, 1], "k": 2}, "expected": 5},
    ),
]


def test_max_consecutive_ones_iii(args, expected):
    solution = Solution()

    assert solution.longestOnes(**args) == expected
