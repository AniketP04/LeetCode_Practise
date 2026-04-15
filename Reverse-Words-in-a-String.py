1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        
8        result = []
9        i = 0
10        n = len(s)
11
12        # Iterate through the string to extract words
13        while i < n:
14
15            # skip the leading spaces
16            while i<n and s[i]==" ":
17                i+=1
18            
19            if i<n:
20                word_start = i
21
22                while i<n and s[i]!=" ":
23                    i+=1
24                result.append(s[word_start:i])
25        return " ".join(result[::-1])
26