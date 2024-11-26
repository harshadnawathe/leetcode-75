from solutions.nearest_exit_from_entrance_in_maze.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "maze": [
                    ["+", "+", ".", "+"],
                    [".", ".", ".", "+"],
                    ["+", "+", "+", "."],
                ],
                "entrance": [1, 2],
            },
            "expected": 1,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "maze": [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]],
                "entrance": [1, 0],
            },
            "expected": 2,
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "maze": [[".", "+"]],
                "entrance": [0, 0],
            },
            "expected": -1,
        },
    ),
]


def test_nearest_exit_from_entrance_in_maze(args, expected):
    solution = Solution()

    assert solution.nearestExit(**args) == expected
