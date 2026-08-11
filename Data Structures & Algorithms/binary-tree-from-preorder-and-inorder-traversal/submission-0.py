# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_track = {val:index for index,val in enumerate(inorder)}

        def build(pre_index,left_bound,right_bound):
            if (left_bound  > right_bound):
                return None
            
            root_val = preorder[pre_index]
            root = TreeNode(root_val)

            mid = inorder_track[root_val]
            left_child_index = pre_index+1
            no_in_left = mid - left_bound
            root.left = build(left_child_index,left_bound,mid-1)
            right_child_index = pre_index + 1+no_in_left
            root.right = build(right_child_index, mid +1, right_bound)
            return root
        return build(0, 0, len(inorder) - 1)
        