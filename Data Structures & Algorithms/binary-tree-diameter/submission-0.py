# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Complexity:
        # Time O(n) since we have to visit each node once 
        # Space: Proportional to the height of the tree O(logn) for a balanced tree O(n) if not balanced
        self.res = 0 

        def dfs(curr): 
            if not curr: 
                return 0 
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, (left+right))
            return max(left, right) + 1 # need to add one to add 1 for the current node that we are at
        dfs(root)
        return self.res