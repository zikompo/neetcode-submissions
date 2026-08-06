class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diffs = [(gas[i]-cost[i]) for i in range(len(gas))]
        res = 0
        total = 0
        i = 0
        while i < len(gas):
            total += diffs[i]
            if total < 0:
                total = 0
                res = i + 1
            i += 1
        return res