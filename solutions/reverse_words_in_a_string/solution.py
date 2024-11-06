from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        chars = list(s)

        # Reverse order of words
        self._reverse(chars, 0, len(chars))

        left, right = 0, 0
        while right < len(chars):
            if chars[right] != " ":
                right += 1
                continue

            self._reverse(chars, left, right)

            while (right < len(chars)) and (chars[right] == " "):
                right += 1

            left = right

        self._reverse(chars, left, len(chars))

        # Trim spaces between words
        i, j, n = 0, 0, 0
        while j < len(chars):
            if chars[j] == " ":
                n += 1
            else:
                n = 0

            if chars[j] != " " or n == 1:
                chars[i] = chars[j]
                i += 1

            j += 1

        chars = chars[:i]

        return "".join(chars)

    def _reverse(self, cs: List, left: int, right: int):
        while left < right:
            right -= 1
            cs[left], cs[right] = cs[right], cs[left]
            left += 1
