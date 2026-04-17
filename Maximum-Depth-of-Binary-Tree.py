1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def maxDepth(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        if root is None:
14            return 0
15        
16        left_depth = self.maxDepth(root.left)
17        right_depth = self.maxDepth(root.right)
18
19        return 1+max(left_depth,right_depth)