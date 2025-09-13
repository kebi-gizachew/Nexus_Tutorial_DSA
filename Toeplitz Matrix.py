class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
            for k in range(len(matrix[0])-1):
                if matrix[i][k]!=matrix[i+1][k+1]:
                    return False
        return True
