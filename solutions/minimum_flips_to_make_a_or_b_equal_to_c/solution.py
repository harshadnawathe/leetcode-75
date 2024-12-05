class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mismatched_bits = (a | b) ^ c

        return mismatched_bits.bit_count() + (mismatched_bits & a & b).bit_count()
