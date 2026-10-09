class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 means no fruit 
        # 1 means good fruit
        # 2 means bad fruit 
        # if 1 is next to 2 and it passes 1 minute it becomes 2 
        # after all fruits are rotten return how many minutes it tooks 
        # O(m * n) time since we have to go at most through the entire grid 
        # O(m * n) space since we have to grow our queue at most the size of the grid
        q = deque()
        fresh = 0 
        minutes = 0
        rows = len(grid)
        columns = len(grid[0])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while fresh > 0 and q:
            length = len(q) #this means how many bad fruits we have so far
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions: 
                    next_row = dr + r
                    next_col = dc + c
                    if ((next_row in range(rows)) and (next_col in range(columns)) and (grid[next_row][next_col] == 1)):
                        grid[next_row][next_col] = 2 # it must now be a rotten fruit 
                        q.append((next_row, next_col)) # update that we have a new rotten fruit 
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1

