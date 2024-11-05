from solutions.kids_with_the_greatest_number_of_candies.solution import Solution


def test_kids_with_the_greatest_number_of_candies():
    solution = Solution()

    assert solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [
        True,
        True,
        True,
        False,
        True,
    ]
    assert solution.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1) == [
        True,
        False,
        False,
        False,
        False,
    ]
    assert solution.kidsWithCandies(candies=[12, 1, 12], extraCandies=10) == [
        True,
        False,
        True,
    ]
