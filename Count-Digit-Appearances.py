1class Solution(object):
2    def countDigitOccurrences(self, nums, digit):
3        """
4        :type nums: List[int]
5        :type digit: int
6        :rtype: int
7        """
8
9        count = 0
10
11        for num in nums:
12            if num==0 and digit==0:
13                count+=1
14            
15            while num>0:
16                if num%10== digit:
17                    count+=1
18                num//=10
19        return count
20        
21        