# generate all subarrays and find sum of all subarrays

def subarray(arr):
    a = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)+1):
            a.append(arr[i:j])
    print("subarrays:",a) #printing subarrays
    subarraySum(arr)
    
    
def subarraySum(arr):
    a = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)+1):
            sum = 0
            for k in range(i,j):
               sum += arr[k]
            a.append(sum)            
    print("sum=",a)

subarray([1,2,3,4])

'''
output
subarrays: [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
sum: [1, 3, 6, 10, 2, 5, 9, 3, 7, 4]
'''
