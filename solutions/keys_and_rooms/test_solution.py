from solutions.keys_and_rooms.solution import Solution

tests = [
    ("Example 1", {"args": {"rooms": [[1], [2], [3], []]}, "expected": True}),
    (
        "Example 2",
        {"args": {"rooms": [[1, 3], [3, 0, 1], [2], [0]]}, "expected": False},
    ),
]


def test_keys_and_rooms(args, expected):
    solution = Solution()

    assert solution.canVisitAllRooms(**args) == expected
