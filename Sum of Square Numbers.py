class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        r=int(c**(0.5))
        i,j=0,r
        while j>=i:
            if j*j + i*i==c:
                return True
            if j*j+i*i>c:
                j-=1
            if j*j+i*i<c:
                i+=1
        return False
