
#207. Course Schedule
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReq = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preReq[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preReq[course] == []:
                return True

            visited.add(course)
            for preC in preReq[course]:
                if not dfs(preC): return False
            visited.remove(course)
            preReq[course] = []
            return True
