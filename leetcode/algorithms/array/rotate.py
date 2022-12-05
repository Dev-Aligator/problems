
class Solution():
    def __init__(self):
        matrix = []
        n = int((input()))
        for i in range(n):
            matrix.append([int(x) for x in input().split()])
        print(self.rotate(matrix))
    def rotate(self, matrix :list[list[int]]):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
Solution()
