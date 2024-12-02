from solutions.find_peak_element.solution import Solution

tests = [
    (
        "Example 1",
        {
            "args": {
                "nums": [1, 2, 3, 1],
            },
            "expected": 2,
        },
    ),
    (
        "Example 2",
        {
            "args": {
                "nums": [1, 2, 1, 3, 5, 6, 4],
            },
            "expected": 5,
        },
    ),
    (
        "Example 3",
        {
            "args": {
                "nums": [1],
            },
            "expected": 0,
        },
    ),
]


def test_find_peak_element(args, expected):
    solution = Solution()

    assert solution.findPeakElement(**args) == expected
