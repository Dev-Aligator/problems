from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        additional_node = 1
        m,n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        additional_node = 0
                    else:
                        matrix[r][0] = 0
        for r in range(1, m):
            if matrix[r][0] == 0:
                matrix[r] = [0] * n
        for c in range(n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0
        if not additional_node:
            matrix[0] = [0] * n
        return matrix

print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
        


