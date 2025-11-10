class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count=0
        q={}
        l=0
        for i,r in enumerate(s):
            if r in q and q[r]>=l:
                l=q[r]+1
            q[r]=i
            max_count=max(max_count,i-l+1)
        return max_count
