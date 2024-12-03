from solutions.combination_sum_iii.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "k": 3,
                "n": 7,
            },
            "expected": [[1, 2, 4]],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "k": 3,
                "n": 9,
            },
            "expected": [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "k": 4,
                "n": 1,
            },
            "expected": [],
        },
    ),
]


def test_combination_sum_iii(args, expected):
    solution = Solution()

    assert solution.combinationSum3(**args) == expected
