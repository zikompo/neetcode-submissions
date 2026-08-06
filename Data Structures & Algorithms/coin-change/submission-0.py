class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount+1)
        
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if cache[amount] != -1:
                return cache[amount]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1+dp(amount-coin))
            cache[amount] = min_coins
            return cache[amount]
        ans = dp(amount)
        return ans if ans != float('inf') else -1