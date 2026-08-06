class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        window = []
        target = threshold * k
        acc = 0
        for r in range(len(arr)):
            window.append(arr[r])
            if r-l+1 > k:
                window.pop(0)
                l += 1
            if r-l+1 == k and sum(window) >= target:
                acc += 1
        return acc