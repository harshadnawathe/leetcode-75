from solutions.string_compression.solution import Solution
from typing import List


def test_string_compression():
    solution = Solution()

    def test_compress(list: List[str], compressed_len: int, compressed: List[str]):
        assert solution.compress(list) == compressed_len
        assert list[:compressed_len] == compressed

    test_compress(
        ["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]
    )
    test_compress(["a"], 1, ["a"])
    test_compress(
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        4,
        ["a", "b", "1", "2"],
    )
