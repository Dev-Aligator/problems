from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        nodes = deque()
        root.val = 0
        nodes.appendleft(root)
        maxDepth = 0
        while nodes:
            node = nodes.pop()
            node.val += 1
            maxDepth = max(node.val, maxDepth)

            if node.left:
                node.left.val = node.val
                nodes.appendleft(node.left)
            if node.right:
                node.right.val = node.val
                nodes.appendleft(node.right)
        return maxDepth


        
