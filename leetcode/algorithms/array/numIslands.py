class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visit = set()
        
        rows, cols = len(grid), len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and ((r,c) not in visit):
                    res+=1
                    self.markAll(grid, r,c ,rows, cols, visit)
                    print(r,c)
        return res

                        

    def markAll(self , grid, r,c , rows, cols ,visit):
        if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == "0":
            return
        visit.add((r,c))
        self.markAll(grid, r+1, c, rows, cols, visit)
        self.markAll(grid, r-1, c, rows, cols, visit)
        self.markAll(grid, r, c+1, rows, cols, visit)
        self.markAll(grid, r, c-1, rows, cols, visit)


print(Solution().numIslands([["1","0","1","1","1"],
                             ["1","0","1","0","1"],
                             ["1","1","1","0","1"]]))

        

