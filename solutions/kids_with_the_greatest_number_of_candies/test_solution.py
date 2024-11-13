from solutions.kids_with_the_greatest_number_of_candies.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"candies": [2, 3, 5, 1, 3], "extraCandies": 3},
            "expected": [
                True,
                True,
                True,
                False,
                True,
            ],
        },
    ),
    (
        "Example 2",
        {
            "args": {"candies": [4, 2, 1, 1, 2], "extraCandies": 1},
            "expected": [
                True,
                False,
                False,
                False,
                False,
            ],
        },
    ),
    (
        "Example 3",
        {
            "args": {"candies": [12, 1, 12], "extraCandies": 10},
            "expected": [
                True,
                False,
                True,
            ],
        },
    ),
]


def test_kids_with_the_greatest_number_of_candies(args, expected):
    solution = Solution()

    assert solution.kidsWithCandies(**args) == expected
