from solutions.total_cost_to_hire_k_workers.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "costs": [17, 12, 10, 2, 7, 2, 11, 20, 8],
                "k": 3,
                "candidates": 4,
            },
            "expected": 11,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "costs": [1, 2, 4, 1],
                "k": 3,
                "candidates": 3,
            },
            "expected": 4,
        },
    ),
]


def test_total_cost_to_hire_k_workers(args, expected):
    solution = Solution()

    assert solution.totalCost(**args) == expected
