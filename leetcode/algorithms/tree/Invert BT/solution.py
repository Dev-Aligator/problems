from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        nodes = deque()
        nodes.appendleft(root)
        while nodes:
            node = nodes.pop()

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)


        return root

