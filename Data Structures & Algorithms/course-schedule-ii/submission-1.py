from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # similar to course schedule, but we are returning a valid ordering
        # we start from the ones with indegree 0
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        taken = []

        # how do i account for multiple courses with indegree 0?

        while queue:
            course = queue.popleft()
            taken.append(course)
            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return taken if len(taken) == numCourses else []
        
