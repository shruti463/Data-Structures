# [0,0,1,1,1,2,2,3,3,4] output:[0,1,2,3,4]
#bruteforce
def remove_dup(arr):
    a=[]
    a.append(arr[0])
    for i in arr:
        if i  not in a :
           a.append(i)
        
    print(a)
        
remove_dup([0,0,1,1,1,2,2,3,3,4])
