class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force solution
        max_p = 0
        for i, price in enumerate(prices):
            for j, price2 in enumerate(prices):
                if i == j:
                    continue
                if j > i:
                    max_p = max(max_p, price2-price)
                
        return max_p