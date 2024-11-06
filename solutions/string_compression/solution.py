from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        w, i = 0, 0
        while i < len(chars):
            char = chars[i]
            chars[w] = char
            w += 1
            i += 1

            count = 1
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            if count > 1:
                for s in [str(c) for c in list(str(count))]:
                    chars[w] = s
                    w += 1

        return w
