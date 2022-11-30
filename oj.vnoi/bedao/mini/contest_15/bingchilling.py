
class Solution():
    def __init__(self):
        n = int(input())
        store = []
        for i in range(n):
            store.append([int(x) for x in input().split()])
        self.price(n, store)
    def price(self, n:int, store:list[list]):
        for i in range(n):
            current_store = store[i]
            pay = int((current_store[2]/(current_store[0]+current_store[1])))*current_store[0]
            pay += min(current_store[2]%(current_store[0]+current_store[1]), current_store[0])
            print(pay*5)

Solution()
