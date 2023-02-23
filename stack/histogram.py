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


#efficient approach
