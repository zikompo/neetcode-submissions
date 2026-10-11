import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task = Counter(tasks)
        count = [-cnt for cnt in task.values()]
        heapq.heapify(count)

        time = 0
        q = deque() # pairs of 

        while count or q:
            time += 1

            if count:
                cnt = 1+ heapq.heappop(count)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(count, q.popleft()[0])
        return time
            