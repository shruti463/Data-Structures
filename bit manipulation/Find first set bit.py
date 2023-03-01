class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        if n==0:
            return 0
        k=0
        while n:
            if n>>k & 1:
                return k+1
            k+=1    
