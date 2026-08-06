class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force solution
        min_price = prices[0]
        max_p = 0
        i = 0
        while i < len(prices):
            if prices[i] < min_price:
                min_price = prices[i]
            max_p = max(max_p, prices[i]-min_price)
            i += 1
        return max_p