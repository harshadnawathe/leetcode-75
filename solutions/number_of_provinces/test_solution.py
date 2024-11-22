from solutions.number_of_provinces.solution import Solution

tests = [
    (
        "Example 1",
        {"args": {"isConnected": [[1, 1, 0], [1, 1, 0], [0, 0, 1]]}, "expected": 2},
    ),
    (
        "Example 2",
        {"args": {"isConnected": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]}, "expected": 3},
    ),
    (
        "Example 3",
        {
            "args": {
                "isConnected": [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
            },
            "expected": 1,
        },
    ),
]


def test_number_of_provinces(args, expected):
    solution = Solution()

    assert solution.findCircleNum(**args) == expected
