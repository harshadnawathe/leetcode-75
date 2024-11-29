from solutions.successful_pairs_of_spells_and_potions.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "spells": [5, 1, 3],
                "potions": [1, 2, 3, 4, 5],
                "success": 7,
            },
            "expected": [4, 0, 3],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "spells": [3, 1, 2],
                "potions": [8, 5, 8],
                "success": 16,
            },
            "expected": [2, 0, 2],
        },
    ),
]


def test_successful_pairs_of_spells_and_potions(args, expected):
    solution = Solution()

    assert solution.successfulPairs(**args) == expected
