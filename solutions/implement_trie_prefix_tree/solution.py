from typing import Optional


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return bool(node and node.is_end)

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, word: str) -> Optional[TrieNode]:
        node = self._root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
