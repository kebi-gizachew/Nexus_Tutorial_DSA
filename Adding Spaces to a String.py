class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        y=0
        r=[]
        for i in range(len(s)):
            if y<len(spaces) and i==spaces[y]:
                r.append(" ")
                y+=1
            r.append(s[i])
        return ''.join(r)
