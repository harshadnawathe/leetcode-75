from solutions.reorder_routes_to_make_all_paths_lead_to_the_city_zero.solution import (
    Solution,
)

tests = [
    (
        "Example 1",
        {
            "args": {"n": 6, "connections": [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]},
            "expected": 3,
        },
    ),
    (
        "Example 2",
        {
            "args": {"n": 5, "connections": [[1, 0], [1, 2], [3, 2], [3, 4]]},
            "expected": 2,
        },
    ),
    (
        "Example 3",
        {
            "args": {"n": 3, "connections": [[1, 0], [2, 0]]},
            "expected": 0,
        },
    ),
]


def test_reorder_routes_to_make_all_paths_lead_to_the_city_zero(args, expected):
    solution = Solution()

    assert solution.minReorder(**args) == expected
