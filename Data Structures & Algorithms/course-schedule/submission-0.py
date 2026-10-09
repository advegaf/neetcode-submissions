class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Complexity: Both space and time share O(V+E) since for time we have to go through max at each vertice and egge and our set can grow at max V+E
        visiting = set() # keep all of the courses along the DFS path
        prereqmap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites: 
            # add all of the courses alongside with their prerequisites into a hashmap so we can have O(1) look up time as a pair 
            prereqmap[course].append(prereq)
        def dfs(course):
            if course in visiting:
                # visiting a course twice == cycle
                return False
            if prereqmap[course] == []:
                #has no preqreqs so its good
                return True
            visiting.add(course)
            for pre in prereqmap[course]:

                if not dfs(pre): return False
            visiting.remove(course)
            prereqmap[course] = []
            return True
        for courses in range(numCourses):
            if not dfs(courses): return False
        return True