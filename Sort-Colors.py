1class Solution(object):
2    def sortColors(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        low = 0
8        mid = 0
9        high = len(nums)-1
10
11        while mid <= high:
12            if nums[mid]==0:
13                nums[low],nums[mid]=nums[mid],nums[low]
14                low+=1
15                mid+=1
16            elif nums[mid]==2:
17                nums[mid],nums[high] = nums[high],nums[mid]
18                high-=1
19            else:
20                mid+=1
21