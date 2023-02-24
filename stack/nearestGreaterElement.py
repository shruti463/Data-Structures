def nextLargerElement(a,n):
     s = []
     arr = []
     for i in range(n-1,-1,-1):
         while len(s) !=0 and s[-1]<=a[i]:
             s.pop()
    
         if len(s)==0:
             s.append(a[i])
             arr.append(0)
         else:
             arr.append(s[-1])
             s.append(a[i])
             
     print(arr) 
    
nextLargerElement([73,74,75,71,69,72,76,73], 8)
