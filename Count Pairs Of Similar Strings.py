class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=Counter()
        n=0
        for i in words:
            m=0
            for k in i:
                m|=1<<ord(k)-97
            n+=c[m]
            c[m]+=1
        return n
            
            
