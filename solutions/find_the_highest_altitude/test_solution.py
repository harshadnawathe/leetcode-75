from solutions.find_the_highest_altitude.solution import Solution


def test_find_the_highest_altitude():
    solution = Solution()

    assert solution.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
