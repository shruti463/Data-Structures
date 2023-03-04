def prefixSum(a):
        for i in range(1,len(a)):
            a[i] = a[i]+a[i-1]
        return a
      
def lazy_propogation(arr):
    a = [0]*15
    for i in arr:
        a[i[0]]+=i[1]  #insert n at given index i
    a = prefixSum(a) #find prefix of the array
    print(a) 
        
        
lazy_propogation([(1,3),(4,2),(0,1)])#(i,n)


'''
output: [1, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
'''
