from solutions.string_compression.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {"chars": ["a", "a", "b", "b", "c", "c", "c"]},
            "expected": {
                "compressed_len": 6,
                "compressed": ["a", "2", "b", "2", "c", "3"],
            },
        },
    ),
    (
        "Example 2",
        {
            "args": {"chars": ["a"]},
            "expected": {"compressed_len": 1, "compressed": ["a"]},
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "chars": [
                    "a",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                ]
            },
            "expected": {"compressed_len": 4, "compressed": ["a", "b", "1", "2"]},
        },
    ),
]


def test_string_compression(args, expected):
    solution = Solution()

    compressed_len = expected["compressed_len"]
    assert solution.compress(**args) == compressed_len
    assert args["chars"][:compressed_len] == expected["compressed"]
