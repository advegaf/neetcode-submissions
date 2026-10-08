# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Complexity: 
        # Time: O(n) since we visit each element in the tree once 
        # Space: O(n) since our queue might be at most n/2
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            current_level = []
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(current_level)
        return result
            