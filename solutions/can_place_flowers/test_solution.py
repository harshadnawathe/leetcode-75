from solutions.can_place_flowers.solution import Solution


def test_can_place_flowers():
    solution = Solution()

    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1) is True
    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2) is False
    assert solution.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0, 1, 0, 0], n=0) is True
