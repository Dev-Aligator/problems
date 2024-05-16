from collections import deque
from typing import Deque, List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = deque()

        level = count = 0
        row_avg = [0]

        nodes.appendleft(root)
        nodes.appendleft(None)

        while nodes:
            node = nodes.pop()
            if node:
                count += 1
                row_avg[level] += node.val 

                if node.left:
                    nodes.appendleft(node.left)
                if node.right:
                    nodes.appendleft(node.right)
            else:
                row_avg[level] /= count
                if nodes:
                    nodes.append(None)
                    count = 0
                    row_avg.append(0)
                    level += 1
        return row_avg

    
        
