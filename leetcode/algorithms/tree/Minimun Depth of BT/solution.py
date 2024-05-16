from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        nodes = deque()
        nodes.appendleft([root, 0])

        while nodes:
            node,count = nodes.pop()
            count += 1
            if not node.left and not node.right:
                return count
            
            if node.left:
                nodes.appendleft([node.left, count])
            if node.right:
                nodes.appendleft([node.right, count])
        return 0

        


