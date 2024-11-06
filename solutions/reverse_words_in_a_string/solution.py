from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)

        # Reverse order of words
        self._reverse(chars, 0, len(chars))

        left, right = 0, 0
        while right < len(chars):
            while (right < len(chars)) and (chars[right] == " "):
                right += 1

            left = right
            while (right < len(chars)) and (chars[right] != " "):
                right += 1

            self._reverse(chars, left, right)

        left, right = 0, 0
        while right < len(chars):
            while (right < len(chars)) and (chars[right] == " "):
                right += 1

            while (right < len(chars)) and (chars[right] != " "):
                chars[left] = chars[right]
                left += 1
                right += 1

            while (right < len(chars)) and (chars[right] == " "):
                right += 1

            if right < len(chars):
                chars[left] = " "
                left += 1

        chars = chars[:left]

        return "".join(chars)

    def _reverse(self, cs: List, left: int, right: int):
        while left < right:
            right -= 1
            cs[left], cs[right] = cs[right], cs[left]
            left += 1
