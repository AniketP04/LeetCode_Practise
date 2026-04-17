1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def sortedArrayToBST(self, nums):
9        """
10        :type nums: List[int]
11        :rtype: Optional[TreeNode]
12        """
13        
14        if not nums:
15            return None
16        
17        mid = len(nums)>>1
18
19        root = TreeNode(nums[mid])
20        root.left = self.sortedArrayToBST(nums[:mid])
21        root.right = self.sortedArrayToBST(nums[mid+1:])
22        return root