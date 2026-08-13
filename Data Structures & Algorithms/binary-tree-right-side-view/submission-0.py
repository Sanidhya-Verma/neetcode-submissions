# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 0
        res = collections.defaultdict(set)
        def view(node,level):
            if not node:
                return 
            view(node.right,level+1)
            if level not in res:
                res[level] = node.val
            view(node.left,level+1)
        view(root,0)
        ans =[]
        for i in range(len(res)):
            ans.append(res[i])
        return ans
        