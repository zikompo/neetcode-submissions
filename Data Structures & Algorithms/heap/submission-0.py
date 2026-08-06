class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap)-1
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        x = self.heap[1]
        self.heap[1] = self.heap.pop()
        
        i = 1
        child = 2*i
        while child < len(self.heap):
            if child+1 < len(self.heap) and self.heap[child] > self.heap[child+1]:
                child += 1
            
            if self.heap[child] >= self.heap[i]:
                break
            
            self.heap[child], self.heap[i] = self.heap[i], self.heap[child]

            i = child
            child = 2*i
        return x

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0]
        for num in nums:
            self.push(num)
        