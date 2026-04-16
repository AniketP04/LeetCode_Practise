1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSymmetric(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        if root is None:
14            return False
15        
16        return self.check_mirror(root.left,root.right)
17        
18    def check_mirror(self,left,right):
19        if left is None and right is None:
20            return True
21        if left is None or right is None:
22            return False
23        if left.val != right.val:
24            return False
25        return self.check_mirror(left.left,right.right) and self.check_mirror(left.right,right.left)
26