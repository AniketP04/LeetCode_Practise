1import math
2
3class Solution(object):
4    def internalAngles(self, sides):
5        sides.sort()
6        a, b, c = sides
7
8        # Triangle validity
9        if a + b <= c:
10            return []
11
12
13        # Law of Cosines
14        A = math.degrees(math.acos((b*b + c*c - a*a) / (2.0*b*c)))
15        B = math.degrees(math.acos((a*a + c*c - b*b) / (2.0*a*c)))
16        C = math.degrees(math.acos((a*a + b*b - c*c) / (2.0*a*b)))
17
18        return sorted([A, B, C])