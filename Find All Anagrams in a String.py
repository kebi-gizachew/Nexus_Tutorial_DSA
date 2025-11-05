class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pcount=Counter(p)
        scount=Counter(s[:len(p)])
        r=[]
        l=0
        if scount==pcount:
            r.append(0)
        for k in range(len(p),len(s)):
            scount[s[k]]+=1
            scount[s[l]]-=1
            if scount[s[l]]==0:
                del scount[s[l]]
            l+=1
            if pcount==scount:
                r.append(l)
        return r
