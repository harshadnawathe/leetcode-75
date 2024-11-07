from solutions.maximum_average_subarray_i.solution import Solution
from pytest import approx


def test_maximum_average_subarray_i():
    solution = Solution()

    assert solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == approx(
        12.75000, rel=1e-5
    )

    assert solution.findMaxAverage([5], 1) == approx(5.00000, rel=1e-5)
