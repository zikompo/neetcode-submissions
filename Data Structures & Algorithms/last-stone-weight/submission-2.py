class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we use a max heap
        # at each step, we take the next two stones and do some math
        # any surviving stone gets pushed back into the heap.

        if len(stones) == 1:
            return stones[0]

        stone = [-stone for stone in stones] # for max heap
        heapq.heapify(stone)

        while len(stone) > 1:
            x = -1 * heapq.heappop(stone)
            y = -1 * heapq.heappop(stone)

            if x == y:
                continue
            heapq.heappush(stone, -1 * max(x-y, y-x))
        
        if stone:
            return -1 * stone[0]
        return 0
        

