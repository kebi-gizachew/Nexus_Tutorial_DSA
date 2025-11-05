class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        i,j=0,len(skill)-1
        skill.sort()
        p=0
        n=skill[0]+skill[-1]
        while j>i:
            if n!=skill[j]+skill[i]:
                return -1
            p+=skill[i]*skill[j]
            i+=1
            j-=1
        return p
