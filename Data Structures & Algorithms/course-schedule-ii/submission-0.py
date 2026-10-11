class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        skill_tree = defaultdict(list)
        for course ,req in prerequisites:
            skill_tree[course].append(req)
        checking = set()
        checked  = set()
        output =[]

        def dfs(course):
            if course in checking:
                return False

            if course in checked:
                return True

            checking.add(course)

# very important error i made the below code cannot be low the add course code above 
# Why just simulate an example of Course A requires B. Course C requires B. Course B requires nothing

            #if skill_tree[course] == []:
                #return True

            for pre in skill_tree[course]:
                if dfs(pre) == False:
                    return False

            checking.remove(course)
            checked.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output

        