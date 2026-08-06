class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        heap.heapify(stones)
        while heap.size() > 1:
            x = heap.pop()
            if heap.size == 1:
                break
            y = heap.pop()
            if x == y:
                continue
            
            elif x < y:
                heap.push(y-x)
            else:
                heap.push(x-y)
        
        if heap.size() == 0:
            return 0
        else:
            return heap.heap[1]

class MaxHeap:

    def __init__(self):
        self.heap = [0]

    def size(self):
        return len(self.heap) - 1
    
    def push(self, item):
        self.heap.append(item)
        i = len(self.heap)-1
        while i > 1:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            else:
                break
            i = i //2
    
    def pop(self):
        if len(self.heap) == 2:
            return self.heap.pop()
        x = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        child = i * 2
        while child < len(self.heap):
            if child+1<len(self.heap) and self.heap[child] < self.heap[child+1]:
                child += 1
            
            if self.heap[child] <= self.heap[i]:
                break
            
            self.heap[child], self.heap[i] = self.heap[i], self.heap[child]
            i *= child
            child = 2 * i
        
        return x
    
    def heapify(self, nums):
        self.heap = [0]
        for num in nums:
            self.push(num)