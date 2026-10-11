from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # one of these problems where you have to create an adjacency list
        # basically checking if we can visit every node
        # visit a path, add to visited set
        # at the end, if visited set is not equal to numCourses, return False
        if not prerequisites:
            return True
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)
        
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1
            for sequel in adj[course]:
                indegree[sequel] -= 1
                if indegree[sequel] == 0:
                    queue.append(sequel)
        
        return taken == numCourses