from solutions.move_zeroes.solution import Solution

tests = [
    ("Example 1", {"args": {"nums": [0, 1, 0, 3, 12]}, "expected": [1, 3, 12, 0, 0]}),
    ("Example 2", {"args": {"nums": [0]}, "expected": [0]}),
]


def test_move_zeroes(args, expected):
    solution = Solution()

    solution.moveZeroes(**args)

    assert args["nums"] == expected
