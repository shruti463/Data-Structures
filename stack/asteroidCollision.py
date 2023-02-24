def collision(arr):
    s=[]
    for i in arr:
        
        if len(s) == 0 or s[-1]<0 or i>0:
            s.append(i)
        else:
            dest = False
            while len(s)!=0 and s[-1]>0:
                t = s[-1]
                if abs(i)> t: 
                    s.pop()
                elif abs(i)< s[-1]: #when i is small and destroyed
                    dest = True
                    break
                else: # when equal
                    s.pop()
                    dest = True
                    break
            if dest==False:
                s.append(i)
    print(s)
            


collision([3,4,5,6,-7,-9,12,40,-24])
