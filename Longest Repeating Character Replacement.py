class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        r={}
        u=0
        m=0
        n=0
        for i in range(len(s)):
            r[s[i]]=1+ r.get(s[i],0)
            m=max(m,r[s[i]])
            while (i+1-u)-m>k:
                r[s[u]]-=1
                u+=1
            n=max(n,i-u+1)
        return n
