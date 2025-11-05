class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        r=piles.sort()
        n=0
        t=len(piles)
        for i in range(t//3,t,2):
            n+=piles[i]
        return n
