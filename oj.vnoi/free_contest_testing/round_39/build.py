
class Solution():
    def __init__(self):
        points = []
        edges = []
        n = int(input())
        for i in range(n):
            x,y = input().split()
            points.append([int(x),int(y)])
        for i in range(n-1):
            for j in range(i+1,n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    n-=1
                else:
                    distance = min(abs(points[i][0] - points[j][0]), abs(points[i][1] - points[j][1]))
                    edges.append([i,j,distance])

        edges.sort(key = lambda tup : tup[2])
        print(self.krusal(edges, n))

    def krusal(self, edges:list[list[int]], n:int) -> int:
        parent = []
        for i in range(n):
            parent.append(i)
        count = 0
        total = 0
        for edge in edges:
            if count == n - 1:
                return total
            if parent[edge[0]] != parent[edge[1]]:
                for x in range(parent[edge[1]] + 1, n):
                    if parent[x] == parent[edge[1]]:
                        parent[x] = parent[edge[0]]
                parent[edge[1]] = parent[edge[0]]
                total += edge[2]
                count+=1
        return total

Solution()

                


                

