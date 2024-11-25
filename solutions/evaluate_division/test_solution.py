from solutions.evaluate_division.solution import Solution
from pytest import approx
from itertools import zip_longest

tests = [
    (
        "Example 1",
        {
            "args": {
                "equations": [["a", "b"], ["b", "c"]],
                "values": [2.0, 3.0],
                "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            },
            "expected": [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "equations": [["a", "b"], ["b", "c"], ["bc", "cd"]],
                "values": [1.5, 2.5, 5.0],
                "queries": [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            },
            "expected": [3.75000, 0.40000, 5.00000, 0.20000],
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "equations": [["a", "b"]],
                "values": [0.5],
                "queries": [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            },
            "expected": [0.50000, 2.00000, -1.00000, -1.00000],
        },
    ),
    (
        "Example 4",
        {
            "args": {
                "equations": [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
                "values": [3.0, 4.0, 5.0, 6.0],
                "queries": [
                    ["x1", "x5"],
                    ["x5", "x2"],
                    ["x2", "x4"],
                    ["x2", "x2"],
                    ["x2", "x9"],
                    ["x9", "x9"],
                ],
            },
            "expected": [360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000],
        },
    ),
]


def test_evaluate_division(args, expected):
    solution = Solution()

    actual = solution.calcEquation(**args)

    for got, want in zip_longest(actual, expected):
        assert got == approx(want, abs=1e-5)
