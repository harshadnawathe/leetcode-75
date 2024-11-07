from solutions.max_number_of_k_sum_pairs.solution import Solution


def test_max_number_of_k_sum_pairs():
    solution = Solution()

    assert solution.maxOperations([1, 2, 3, 4], 5) == 2
    assert solution.maxOperations([3, 1, 3, 4, 3], 6) == 1
    assert solution.maxOperations([1, 2, 3, 4], 10) == 0
    assert solution.maxOperations([3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2], 1) == 0
    assert (
        solution.maxOperations(
            [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3
        )
        == 4
    )
