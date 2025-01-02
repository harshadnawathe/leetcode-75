from typing import List
from itertools import accumulate
from operator import add


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        is_vowel_str = [s[0] in vowels and s[-1] in vowels for s in words]
        vowel_str_count = [0] + list(accumulate(is_vowel_str, add))

        return [vowel_str_count[e + 1] - vowel_str_count[b] for b, e in queries]
