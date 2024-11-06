from solutions.increasing_triplet_subsequence.solution import Solution


def test_increasing_triplet_subsequence():
    solution = Solution()

    assert solution.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert solution.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert solution.increasingTriplet([2, 1, 5, 0, 4, 6]) is True
