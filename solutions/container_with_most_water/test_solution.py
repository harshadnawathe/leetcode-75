from solutions.container_with_most_water.solution import Solution


def test_container_with_most_water():
    solution = Solution()

    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1
