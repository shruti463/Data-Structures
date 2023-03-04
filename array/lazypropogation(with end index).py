def prefixSum(a):
        for i in range(1,len(a)):
            a[i] = a[i]+a[i-1]
        return a
#bruteforce
# def lazy_propogation(arr):
#     a=[0]*15
#     for i in arr:
#         for j in range(i[0],i[1]+1):
#             a[j]+= i[2]
  
#     print(a)
        
        
def lazy_propogation(arr):
    a=[0]*15
    for i in arr:
        a[i[0]] +=i[2]
        a[i[1]+1] -= i[2] # at e+1 add -ve n so in prefix sum it will cancel out
    a = prefixSum(a)
    print(a)
    
lazy_propogation([(2,4,2),(1,3,1),(0,2,3),(4,6,1)])  #(s,e,n)


'''
output: [3, 4, 6, 3, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
'''
