# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        res = collections.defaultdict(list)
        def travel(node,level):
            if not node:
                return 
            res[level].append(node.val)
            travel(node.left,level+1)
            travel(node.right,level+1)

        travel(root,0)
        ans =[]
        for i in range(len(res)):
            ans.append(res[i])
        return ans

        