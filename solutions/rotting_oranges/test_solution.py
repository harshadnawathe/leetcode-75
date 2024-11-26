from solutions.rotting_oranges.solution import Solution

tests = [
    ("Example 1", {"args": {"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}, "expected": 4}),
    (
        "Example 2",
        {"args": {"grid": [[2, 1, 1], [0, 1, 1], [1, 0, 1]]}, "expected": -1},
    ),
    ("Example 3", {"args": {"grid": [[0, 2]]}, "expected": 0}),
]


def test_rotting_oranges(args, expected):
    solution = Solution()

    assert solution.orangesRotting(**args) == expected
