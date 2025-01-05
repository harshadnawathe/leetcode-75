from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff_array = [0] * (len(s) + 1)

        for start, end, dir in shifts:
            diff_array[start] += 1 if dir else -1
            diff_array[end + 1] += -1 if dir else 1

        shifted_chars = []
        shift = 0
        for i, char in enumerate(s):
            shift = (shift + diff_array[i]) % 26
            shifted_chars.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))

        return "".join(shifted_chars)
