class Solution:
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        return self.rangeBitwiseAnd(m>>1, n>>1) << 1

  
