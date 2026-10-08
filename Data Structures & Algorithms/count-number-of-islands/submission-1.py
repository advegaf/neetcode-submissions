class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # there are no solutions
        if not grid: 
            return 0 
        

        rows = len(grid)
        cols = len(grid[0])

        islands = 0 
        visited = set()

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0, -1]] 

                for dr, dc in directions:
                    rd = r + dr
                    cd = c + dc
                    if (rd in range(rows)) and (cd in range(cols)) and (grid[rd][cd] == "1") and ((rd, cd) not in visited): 
                        q.append((rd, cd))
                        visited.add((rd, cd))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

        # Complexity: 
        # Time: O(n) since we visit each element in the tree once 
        # Space: O(n) since our queue might be at most n/2