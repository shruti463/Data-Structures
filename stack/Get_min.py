import stack as node

def getMin(strr):
    minval = -1
    for i in strr:
        if s1.isEmpty() and s2.isEmpty():
            s1.push(i)
            s2.push(i)
            minval = s2.peek()
        else:
            s1.push(i)
            if i <= s2.peek():
                s2.push(i)
                minval = s2.peek()
    return minval

def popStrr():
    if s1.isEmpty() and s2.isEmpty():
        return -1
    data = s1.pop()
    minval = s2.peek()
    if data == minval:
        s2.pop()
        minval = s2.peek()
    return minval

if __name__ == "__main__":
    s1 = node.stack() #main stack
    s2 = node.stack() #min stack

    strr= [10,20,9,15,16,2,2]
    print("min before:",getMin(strr))
    print("min after:",popStrr())
    
