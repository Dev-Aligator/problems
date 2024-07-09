from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows_upper, cols_upper = len(matrix), len(matrix[0])
        rows_lower, cols_lower = 0, 0
        res = []
        pointer = "top"
        while rows_lower != rows_upper  and cols_lower != cols_upper:
            if pointer == "top":
                res += matrix[rows_lower][cols_lower:cols_upper]
                pointer = "right"
                rows_lower += 1
            elif pointer == "right":
                for i in range(rows_lower, rows_upper):
                    res.append(matrix[i][cols_upper-1])
                pointer = "bottom"
                cols_upper -= 1
            elif pointer == "bottom":
                res += list(reversed(matrix[rows_upper - 1][cols_lower:cols_upper]))
                pointer = "left"
                rows_upper -= 1
            else:
                for i in range(rows_upper - 1, rows_lower - 1, -1):
                    res.append(matrix[i][cols_lower])
                pointer = "top"
                cols_lower += 1
        return res

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
                




             
