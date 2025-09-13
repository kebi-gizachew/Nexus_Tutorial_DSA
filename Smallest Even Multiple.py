class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """.
        m=n
        while m>=n:
            if m%2==0:
                return m
            m*=2
        
