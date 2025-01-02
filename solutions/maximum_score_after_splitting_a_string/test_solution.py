from solutions.maximum_score_after_splitting_a_string.solution import Solution

tests = [
    (
        "Example 1",
        {"args": {"s": "011101"}, "expected": 5},
    ),
    (
        "Example 2",
        {"args": {"s": "00111"}, "expected": 5},
    ),
    (
        "Example 3",
        {"args": {"s": "1111"}, "expected": 3},
    ),
    (
        "Example 4",
        {"args": {"s": "00"}, "expected": 1},
    ),
]


def test_maximum_score_after_splitting_a_string(args, expected):
    solution = Solution()

    assert solution.maxScore(**args) == expected
