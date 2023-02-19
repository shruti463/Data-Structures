import stack as node
def maxSum(s1,s2,s3):
    while True:
        if s1.isEmpty() or s2.isEmpty() or s3.isEmpty():
            return -1
        elif s1.peek()>=s2.peek() and s1.peek()>s3.peek():
            s1.pop()
        elif s2.peek()>s1.peek() and s2.peek()>=s3.peek():
            s2.pop()
        elif s3.peek()>=s1.peek() and s3.peek()>s2.peek():
            s3.pop()
        
        elif s1.peek() == s2.peek() and s2.peek() == s3.peek():
            return s1.peek()
        else:
            return -1
    

s1 = node.stack()
s2 = node.stack()
s3 = node.stack()

a1 = [0,0,1]
a2 = [1,1,2]
a3 = [2,0]

s1.sum(a1,s1)
s2.sum(a2, s2)
s3.sum(a3, s3)

print(maxSum(s1,s2,s3))   #-1
