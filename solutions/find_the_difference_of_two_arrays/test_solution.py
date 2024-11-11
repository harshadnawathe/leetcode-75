from solutions.find_the_difference_of_two_arrays.solution import Solution
import pytest
from typing import List


tests = [
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
]


@pytest.mark.parametrize("nums1,nums2,want", tests)
def test_find_the_difference_of_two_arrays(
    nums1: List[int], nums2: List[int], want: List[List[int]]
):
    solution = Solution()

    got = solution.findDifference(nums1, nums2)

    assert len(got) == len(want)
    for i in range(len(want)):
        assert sorted(got[i]) == sorted(want[i])
