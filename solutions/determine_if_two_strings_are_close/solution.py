from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        cc1 = self.char_counts(word1)
        cc2 = self.char_counts(word2)

        for i in range(len(cc1)):
            if (cc1[i] != cc2[i]) and (cc1[i] == 0 or cc2[i] == 0):
                return False

        cc1.sort()
        cc2.sort()

        return cc1 == cc2

    def char_counts(self, s: str) -> List[int]:
        counts = [0] * 26

        for char in s:
            counts[ord(char) - ord("a")] += 1

        return counts
