def countSetBits(n):
        count = 0
        while n!=0:
            if n&1==1:
                count +=1
            n = n>>1
print(countSetBits(5))

#brian kernigam algo (optimized solution)
def count(n):
    result = 0
    while n:
        n = n&(n-1)
        result +=1
    return result
print(count(5))
