class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # create adjacency list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            