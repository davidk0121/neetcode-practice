class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxRes = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                sum = prices[r] - prices[l]
                maxRes = max(sum, maxRes)
                r += 1
            else:
                l = r 
                r += 1
        return maxRes