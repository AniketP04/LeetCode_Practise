1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSameTree(self, p, q):
9        """
10        :type p: Optional[TreeNode]
11        :type q: Optional[TreeNode]
12        :rtype: bool
13        """
14
15        if p is None and q is None:
16            return True
17        
18        if p is None or q is None:
19            return False
20        
21        if p.val == q.val:
22            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
23        return False
24        
25
26        