1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isBalanced(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        def check_height(node):
14            if node is None:
15                return 0
16            
17            left_height = check_height(node.left)
18            right_height = check_height(node.right)
19
20            if (left_height == -1 or right_height == -1 or abs(left_height-right_height)>1):
21                return -1
22            return 1+max(left_height,right_height)
23        
24        return check_height(root) >= 0