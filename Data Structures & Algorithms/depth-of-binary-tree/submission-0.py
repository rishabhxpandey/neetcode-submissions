# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        base case
        recurse
        '''

        if not root:
            return 0

        '''
        depth of 1 is 1 + max(depth of left, depth of right)
        '''
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))