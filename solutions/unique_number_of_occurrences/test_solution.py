from typing import List
from solutions.unique_number_of_occurrences.solution import Solution
import pytest

tests = [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
]


@pytest.mark.parametrize("arr,is_uniq", tests)
def test_unique_number_of_occurrences(arr: List[int], is_uniq: bool):
    solution = Solution()

    assert solution.uniqueOccurrences(arr) == is_uniq
