1class Solution(object):
2    def trafficSignal(self, timer):
3        """
4        :type timer: int
5        :rtype: str
6        """
7        if timer==0:
8            return "Green"
9        elif timer==30:
10            return "Orange"
11        elif 30<timer<=90 : 
12            return "Red"
13        else :
14            return "Invalid"