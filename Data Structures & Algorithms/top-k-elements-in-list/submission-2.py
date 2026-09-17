from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can use counters
        counts = Counter(nums)
        sorted_counts = sorted(counts, key=counts.get, reverse=True)
        return sorted_counts[:k]