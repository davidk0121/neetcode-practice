class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2

            cal = 0
            for p in piles:
                cal += math.ceil(p/k)
            if cal <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res