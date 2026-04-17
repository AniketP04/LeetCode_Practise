1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def minDepth(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        if root is None:
14            return 0
15        
16        if root.left is None:
17            return 1+self.minDepth(root.right)
18
19        if root.right is None:
20            return 1+self.minDepth(root.left)
21
22        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
23        