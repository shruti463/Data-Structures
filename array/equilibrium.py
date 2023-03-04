'''
Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
'''

class Solution:
  #this is the prefix sum of the array
    def prefixSum(self,a):
        for i in range(1,len(a)):
            a[i] = a[i]+a[i-1]
        return a
      
      
      
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        l_sum = 0
        r_sum = 0

        arr = self.prefixSum(A) #prefix array
        for i in range(0,N): 
            if i==0: #when we have first element then left sum is always 0  and right sum is total sum - sum at ith element
                l_sum = 0
                r_sum=arr[N-1] - arr[i]
            else:
                l_sum = arr[i-1]
                r_sum = arr[N-1] - arr[i]
            if r_sum == l_sum:
                return i+1       #  1 based indexing
        return -1
