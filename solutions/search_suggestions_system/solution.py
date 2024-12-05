from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = TrieNode()

        for product in products:
            node = trie
            for char in product:
                node = node.children.setdefault(char, TrieNode())
                node.add_suggestion(product)

        suggestions = []
        node = trie
        for char in searchWord:
            if char not in node.children:
                break
            node = node.children[char]
            suggestions.append(node.suggestions)

        for _ in range(len(suggestions), len(searchWord)):
            suggestions.append([])

        return suggestions


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.suggestions = []

    def add_suggestion(self, product):
        self.suggestions.append(product)
        self.suggestions.sort()
        self.suggestions = self.suggestions[:3]
