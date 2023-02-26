#bruteforce approach

def histo(arr):
    cur =0
    res=0
    for i in range(len(arr)):
        cur  = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>= arr[i]:
                cur +=arr[i]
            else:
                break
        for j in range(i+1,len(arr)):
            if arr[j]>= arr[i]:
                cur +=arr[i]
            else:
                break
        res = max(res, cur)
    return res
print(histo([6,2,5,4,1,5,6]))


#efficient approach(TLE)
def NSL(arr , i):
    for j in  range (i ,-1,-1):
        if arr[j]< arr[i]:
            return j+1
    return 0

def NSR(arr,i):
    for j in  range (i , len(arr)):
        if arr[j]< arr[i]:
            return j-1
    return len(arr)-1

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr = heights
        n = len(arr)
        res = 0
        for i in range(n):
            a = NSL(arr,i)
            b = NSR(arr, i)

            res = max(res, (b-a+1)*arr[i])
        return res
    

        
