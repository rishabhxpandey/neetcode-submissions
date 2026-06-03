# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        some sort of traversal where we keep track of largest node we see
        counter to track good nodes

            3  -> 1
           /
          3
         / \
        4   2


        '''
        if not root:
            return 0

        self.good_nodes = 0

        def recurse(root, largest_seen):
            if root.val >= largest_seen:
                self.good_nodes += 1
            
            largest_seen = max(largest_seen, root.val)
            if root.left:
                recurse(root.left, largest_seen)
            if root.right:
                recurse(root.right, largest_seen)
        
        recurse(root, root.val)
        return self.good_nodes
