'''
Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 
Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
'''
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        if D<N:
            self.reverse(A,0,D-1)
            self.reverse(A,D,N-1)
            self.reverse(A,0,N-1)
        else: 
            D=D%N
            self.reverse(A,0,D-1)
            self.reverse(A,D,N-1)
            self.reverse(A,0,N-1)
            
        return A
        
    def reverse(self,arr, l, h):
        while l<h:
            arr[l], arr[h] = arr[h], arr[l]
            l = l+1
            h=h-1
