class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a=min(len(nums1),len(nums2))
        for i in range(a):
            if nums1[i] in nums2:
                return nums1[i]
        return -1
