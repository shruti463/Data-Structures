def posOfRightMostSetBit(n):
        if n==0:
            return 0
        k=0
       
        while n:
            if (n>>k & 1):
                return k #sending index
            k+=1    
def twoOddNum(arr):
    xor = 0
    for i in arr:
        xor = i^xor
    setbit = posOfRightMostDiffBit(xor)
    arr1=xor
    arr2=xor
    for i in arr:
        if (i>>setbit)&(1)==1:
            arr1 =arr1^i
            
        elif (i>>setbit)&(1)==0:
            arr2 =arr2^i
    return arr1, arr2

        
    
    
        
print(twoOddNum([4, 2, 4, 5, 2, 3, 3, 1]))
