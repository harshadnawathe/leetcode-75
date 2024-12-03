from solutions.letter_combinations_of_a_phone_number.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "digits": "23",
            },
            "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "digits": "",
            },
            "expected": [],
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "digits": "2",
            },
            "expected": ["a", "b", "c"],
        },
    ),
]


def test_letter_combinations_of_a_phone_number(args, expected):
    solution = Solution()

    assert solution.letterCombinations(**args) == expected
