from collections import defaultdict


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        char_value = defaultdict(int, {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1})
        max_diff = diff = 0

        for i in range(len(s) - k):
            diff += char_value[s[i + k]] - char_value[s[i]]
            if max_diff < diff:
                max_diff = diff

        return sum([char_value[char] for char in s[:k]]) + max_diff
