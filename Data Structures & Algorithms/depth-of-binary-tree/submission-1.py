# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:   
        # DFS Recursion: O(n) time complexity since we have to go through the entire list, for time complexity it is O(k) where k is the height of the tree but it can be O(n) worst case if it is unbalanced
        '''
        if not root: 
            return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # Breath First Search (level order traversal)
        if not root: 
            return 0
            
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)): 
                node = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            level += 1
        return level
        '''
        # Iterative DFS
        stack = [[root, 1]]
        maxdepth = 0
        while stack: 
            node, depth = stack.pop()
            if node: 
                maxdepth = max(maxdepth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return maxdepth 
        # Time is O(n) since we have to traverse through the entire tree, space is O(n) since our stack can grow at max the entire size of the tree which is n 
