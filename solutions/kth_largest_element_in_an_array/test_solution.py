from solutions.kth_largest_element_in_an_array.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [3, 2, 1, 5, 6, 4], "k": 2}, "expected": 5}),
    (
        "Example 2",
        {"args": {"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4}, "expected": 4},
    ),
]


def test_kth_largest_element_in_an_array(args, expected):
    solution = Solution()

    assert solution.findKthLargest(**args) == expected
