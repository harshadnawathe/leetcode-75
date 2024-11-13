from solutions.determine_if_two_strings_are_close.solution import Solution

tests = [
    ("Example 1", {"args": {"word1": "abc", "word2": "bca"}, "expected": True}),
    ("Example 2", {"args": {"word1": "a", "word2": "aa"}, "expected": False}),
    ("Example 3", {"args": {"word1": "cabbba", "word2": "abbccc"}, "expected": True}),
    ("Example 4", {"args": {"word1": "uau", "word2": "ssx"}, "expected": False}),
    (
        "Example 5",
        {
            "args": {
                "word1": "aaabbbbccddeeeeefffff",
                "word2": "aaaaabbcccdddeeeeffff",
            },
            "expected": False,
        },
    ),
]


def test_determine_if_two_strings_are_close(args, expected):
    solution = Solution()

    assert solution.closeStrings(**args) == expected
