from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        nodes = deque()
        nodes.append([root, str(root.val)])

        while nodes:
            node, path = nodes.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                nodes.append([node.left, path + "->" + str(node.left.val)])
            if node.right:
                nodes.append([node.right, path + "->" + str(node.right.val)])
        return res

