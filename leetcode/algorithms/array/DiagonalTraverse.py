class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]):
        nrow, ncol = len(mat), len(mat[0])
        store = [[] for _ in range(nrow + ncol - 1)]

        for x in range(nrow):
            for y in range(ncol):
                value = mat[x][y]
                store[x + y].append(value)
        res = []
        
        for i in range(nrow + ncol - 1):
            res += store[i] if i % 2 else list(reversed(store[i]))

        return res

        
          
            
print(Solution().findDiagonalOrder(mat=[[1,2,3],[4,5,6],[7,8,9]]))
