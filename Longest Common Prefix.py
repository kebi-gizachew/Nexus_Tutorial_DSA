class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=""
        t=len(strs[0])
        for i in range(len(strs)-1):
            for k in range(min(len(strs[i]),len(strs[i+1]))):
                if strs[i][k]==strs[i+1][k]:
                    s+=strs[i][k]
                else:
                    break
            strs[i+1]=s
            s=""
        return strs[-1]


        
