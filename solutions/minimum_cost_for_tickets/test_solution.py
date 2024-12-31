from solutions.minimum_cost_for_tickets.solution import Solution

tests = [
    (
        "Example 1",
        {"args": {"days": [1, 4, 6, 7, 8, 20], "costs": [2, 7, 15]}, "expected": 11},
    ),
    (
        "Example 2",
        {
            "args": {
                "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
                "costs": [2, 7, 15],
            },
            "expected": 17,
        },
    ),
]


def test_minimum_cost_for_tickets(args, expected):
    solution = Solution()

    assert solution.mincostTickets(**args) == expected
