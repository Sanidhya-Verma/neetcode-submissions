# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        steps = 0
        ans = 0

        def counter(node):
            nonlocal steps,ans
            if not node:
                return 

            counter(node.left)

            steps+=1
            if steps == k:
                ans = node.val
                return ans

            counter(node.right)
        counter(root)
        return ans
        