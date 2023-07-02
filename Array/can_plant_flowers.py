class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        (ppf, pf) = (0, flowerbed[0])
        for flower in flowerbed[1:] + [0]:
            if (not ppf) and (not pf) and not (flower):
                pf = 1
                c += 1
            ppf = pf
            pf = flower
        return c >= n
