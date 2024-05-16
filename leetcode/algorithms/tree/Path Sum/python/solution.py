from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        nodes = deque()
        nodes.append([root, 0])

        while nodes:
            node, pathSum = nodes.pop()
            pathSum += node.val

            if not node.left and not node.right and pathSum == targetSum:
                return True
            if node.left:
                nodes.append([node.left, pathSum])
            if node.right:
                nodes.append([node.right, pathSum])
        return False



        
