from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cc1 = Counter(word1)
        cc2 = Counter(word2)

        keys1 = set(cc1.keys())
        keys2 = set(cc2.keys())

        sorted_vals1 = sorted(cc1.values())
        sorted_vals2 = sorted(cc2.values())

        return sorted_vals1 == sorted_vals2 and keys1 == keys2
