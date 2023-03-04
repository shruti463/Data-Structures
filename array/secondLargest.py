'''
Given an array Arr of size N, print second largest distinct element from an array.

Example 1:

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
'''

class Solution:

	def print2largest(self,arr, n):
		# code here
		first = 0
		second = 0
		for i in arr:
		    if i > first and i> second:
		        second = first
		        first = i
		    elif i< first and i > second:
		        second = i 
		if second ==0:
		    return -1
    return second
'''
Input: 
21
642 642 642 642 642 642 642 642 642 642 642 642 642 642 642 642 642 642 642 642 642

Output: 
-1
'''
		     
