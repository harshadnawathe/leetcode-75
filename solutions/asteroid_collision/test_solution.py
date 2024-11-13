from solutions.asteroid_collision.solution import Solution

tests = [
    ("Example 1", {"args": {"asteroids": [5, 10, -5]}, "expected": [5, 10]}),
    ("Example 2", {"args": {"asteroids": [8, -8]}, "expected": []}),
    ("Example 3", {"args": {"asteroids": [10, 2, -5]}, "expected": [10]}),
]


def test_asteroid_collision(args, expected):
    solution = Solution()

    assert solution.asteroidCollision(**args) == expected
