1class Solution(object):
2    def validPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7    
8        def is_palindrome(left, right):
9            while left<right:
10                if s[left]!=s[right]:
11                    return False
12                left+=1
13                right-=1
14            return True
15        
16        left, right = 0, len(s)-1
17
18        while left<right:
19            if s[left]!=s[right]:
20                return is_palindrome(left,right-1) or is_palindrome(left+1,right)
21            
22            left+=1
23            right-=1
24        
25        return True