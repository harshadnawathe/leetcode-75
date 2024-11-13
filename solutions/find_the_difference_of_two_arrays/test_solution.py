from solutions.find_the_difference_of_two_arrays.solution import Solution


tests = [
    (
        "Example 1",
        {
            "args": {"nums1": [1, 2, 3], "nums2": [2, 4, 6]},
            "expected": [[1, 3], [4, 6]],
        },
    ),
    (
        "Example 2",
        {"args": {"nums1": [1, 2, 3, 3], "nums2": [1, 1, 2, 2]}, "expected": [[3], []]},
    ),
]


def test_find_the_difference_of_two_arrays(args, expected):
    solution = Solution()

    got = solution.findDifference(**args)

    assert len(got) == len(expected)
    for i in range(len(expected)):
        assert sorted(got[i]) == sorted(expected[i])
