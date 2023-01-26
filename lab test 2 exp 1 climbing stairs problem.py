class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        
        a = int(3)
        b = int(2)
        
        while(n-3 > 0):
            a = a + b
            b = a - b
            n -= 1
        return a

    print( a)
