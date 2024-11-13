from solutions.can_place_flowers.solution import Solution

tests = [
    ("Example 1", {"args": {"flowerbed": [1, 0, 0, 0, 1], "n": 1}, "expected": True}),
    ("Example 2", {"args": {"flowerbed": [1, 0, 0, 0, 1], "n": 2}, "expected": False}),
    (
        "Example 3",
        {"args": {"flowerbed": [0, 0, 0, 0, 0, 1, 0, 0], "n": 0}, "expected": True},
    ),
]


def test_can_place_flowers(args, expected):
    solution = Solution()

    assert solution.canPlaceFlowers(**args) == expected
