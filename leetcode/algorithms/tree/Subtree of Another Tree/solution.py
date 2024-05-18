from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_identical(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return node1.val == node2.val and check_identical(node1.left, node2.left) and check_identical(node1.right, node2.right)


        nodes = deque()
        nodes.appendleft(root)

        while nodes:
            node = nodes.pop()
            if node.val == subRoot.val and check_identical(node, subRoot):
                return True
            
            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

        return False




