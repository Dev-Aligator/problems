from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        
        tasksCount = Counter(tasks)
        tasksCount = list(tasksCount.values())
        maxCounts =  max(tasksCount)
        maxCountsApperance = tasksCount.count(maxCounts)
        maxIdles = (maxCounts - 1) * (n - maxCountsApperance  + 1 )
        idle = max(0, maxIdles - len(tasks) + maxCounts * maxCountsApperance )
        return len(tasks) + idle
            
            
            
print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
