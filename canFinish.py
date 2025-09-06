
#207. Course Schedule
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReq = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preReq[course].append(pre)

        visited = set()
