import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self._smallest = 1
        self._min_heap = []
        self._added_back = set()

    def popSmallest(self) -> int:
        if self._min_heap:
            self._added_back.remove(self._min_heap[0])
            return heapq.heappop(self._min_heap)
        else:
            result = self._smallest
            self._smallest += 1
            return result

    def addBack(self, num: int) -> None:
        if num < self._smallest and num not in self._added_back:
            self._added_back.add(num)
            heapq.heappush(self._min_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
