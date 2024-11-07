from typing import List
from solutions.move_zeroes.solution import Solution


def test_move_zeroes():
    solution = Solution()

    def test(list: List[int], want: List[int]):
        solution.moveZeroes(list)
        assert list == want

    test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    test([0], [0])
