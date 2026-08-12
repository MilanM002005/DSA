class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix), len(matrix[0])
        t = [0]*(n+1)
        maxlength = 0
        prev = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = t[j]
                if matrix[i-1][j-1] == '1':
                    t[j] = min(t[j], t[j-1], prev)+1
                    maxlength = max(maxlength, t[j])
                else:
                    t[j] = 0
                prev = temp
        return maxlength * maxlength
