class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=list(s)
        i,j=0,len(s)-1
        r="aeiouAEIOU"
        while j>i:
            if arr[j] not in r:
                j-=1
            elif arr[i] not in r:
                i+=1
            else:
                arr[j],arr[i]=arr[i],arr[j]
                i+=1
                j-=1
        return ''.join(arr)
