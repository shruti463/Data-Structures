class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        if n==m:
            return -1
        k=0
        n = n^m
        while n:
            if (n>>k & 1):
                return k+1
            k+=1    
