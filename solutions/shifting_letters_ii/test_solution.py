from solutions.shifting_letters_ii.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"s": "abc", "shifts": [[0, 1, 0], [1, 2, 1], [0, 2, 1]]},
            "expected": "ace",
        },
    ),
    (
        "Example 2",
        {
            "args": {"s": "dztz", "shifts": [[0, 0, 0], [1, 1, 1]]},
            "expected": "catz",
        },
    ),
]


def test_shifting_letters_ii(args, expected):
    solution = Solution()

    assert solution.shiftingLetters(**args) == expected
