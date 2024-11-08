from solutions.max_consecutive_ones_iii.solution import Solution


def test_max_consecutive_ones_iii():
    solution = Solution()

    assert solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert (
        solution.longestOnes(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
        )
        == 10
    )
    assert solution.longestOnes([1, 1, 1, 0, 0, 0, 0, 0, 1], 2) == 5
