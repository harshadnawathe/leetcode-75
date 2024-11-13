from solutions.maximum_average_subarray_i.solution import Solution
from pytest import approx

tests = [
    (
        "Example 1",
        {"args": {"nums": [1, 12, -5, -6, 50, 3], "k": 4}, "expected": 12.75000},
    ),
    ("Example 2", {"args": {"nums": [5], "k": 1}, "expected": 5.00000}),
]


def test_maximum_average_subarray_i(args, expected):
    solution = Solution()

    assert solution.findMaxAverage(**args) == approx(expected, rel=1e-5)
