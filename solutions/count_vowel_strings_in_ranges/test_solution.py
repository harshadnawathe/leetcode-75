from solutions.count_vowel_strings_in_ranges.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "words": ["aba", "bcb", "ece", "aa", "e"],
                "queries": [[0, 2], [1, 4], [1, 1]],
            },
            "expected": [2, 3, 0],
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "words": ["a", "e", "i"],
                "queries": [[0, 2], [0, 1], [2, 2]],
            },
            "expected": [3, 2, 1],
        },
    ),
]


def test_count_vowel_strings_in_ranges(args, expected):
    solution = Solution()

    assert solution.vowelStrings(**args) == expected
