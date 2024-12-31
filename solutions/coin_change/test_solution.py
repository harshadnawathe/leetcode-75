from solutions.coin_change.solution import Solution

tests = [
    ("Example 1", {"args": {"coins": [1, 2, 5], "amount": 11}, "expected": 3}),
    ("Example 2", {"args": {"coins": [2], "amount": 3}, "expected": -1}),
    ("Example 3", {"args": {"coins": [1], "amount": 0}, "expected": 0}),
    (
        "Example 4",
        {"args": {"coins": [186, 419, 83, 408], "amount": 6249}, "expected": 20},
    ),
]


def test_coin_change(args, expected):
    solution = Solution()

    assert solution.coinChange(**args) == expected
