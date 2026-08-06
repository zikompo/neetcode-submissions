class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices[:]
            for flight in flights:
                s, d, p = flight[0], flight[1], flight[2]
                temp_prices[d] = min(temp_prices[d], prices[s]+p)
            prices = temp_prices[:]
        return prices[dst] if prices[dst] != float('inf') else -1
            
            
          

