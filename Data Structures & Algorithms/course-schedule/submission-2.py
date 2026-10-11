from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        skill_tree = defaultdict(list)
        for course ,req in prerequisites:
            skill_tree[course].append(req)
        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if skill_tree[course] == []:
                return True

            visited.add(course)

# very important error i made the below code cannot be low the add course code above 
# Why just simulate an example of 
            #if skill_tree[course] == []:
                #return True

            for pre in skill_tree[course]:
                if dfs(pre) == False:
                    return False

            visited.remove(course)

            skill_tree[course] = [] # V-Imp optimization i was not able to think this 

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True


        