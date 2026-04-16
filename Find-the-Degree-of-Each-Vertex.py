1class Solution(object):
2    def findDegrees(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: List[int]
6        """
7        n = len(matrix)
8        result = [0]*n
9
10        for i in range(n):
11            degree = 0 
12            for j in range(n):
13                if matrix[i][j]==1:
14                    degree+=1
15            result[i]=degree
16        return result