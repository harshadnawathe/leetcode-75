from solutions.minimum_cost_to_acquire_required_items.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "cost1": 3,
                "cost2": 2,
                "costBoth": 1,
                "need1": 3,
                "need2": 2,
            },
            "expected": 3,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "cost1": 5,
                "cost2": 4,
                "costBoth": 15,
                "need1": 2,
                "need2": 3,
            },
            "expected": 22,
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "cost1": 5,
                "cost2": 4,
                "costBoth": 15,
                "need1": 0,
                "need2": 0,
            },
            "expected": 0,
        },
    ),
]


def test_minimum_cost_to_acquire_required_items(args, expected):
    solution = Solution()

    assert solution.minimumCost(**args) == expected
