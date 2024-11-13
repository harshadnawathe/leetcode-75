from solutions.max_number_of_k_sum_pairs.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [1, 2, 3, 4], "k": 5}, "expected": 2}),
    ("Example 2", {"args": {"nums": [3, 1, 3, 4, 3], "k": 6}, "expected": 1}),
    ("Example 3", {"args": {"nums": [1, 2, 3, 4], "k": 10}, "expected": 0}),
    (
        "Example 4",
        {
            "args": {"nums": [3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2], "k": 1},
            "expected": 0,
        },
    ),
    (
        "Example 5",
        {
            "args": {
                "nums": [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2],
                "k": 3,
            },
            "expected": 4,
        },
    ),
]


def test_max_number_of_k_sum_pairs(args, expected):
    solution = Solution()

    assert solution.maxOperations(**args) == expected
