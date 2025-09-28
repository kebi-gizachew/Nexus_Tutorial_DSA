class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        c=Counter(words[0])
        for i in words[1:]:
            c&=Counter(i)
        return list(c.elements())

                
        
