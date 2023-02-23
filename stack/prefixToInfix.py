def prefixToInfix(exp):
        precedence = {"^":3, "+":1, "-":1 ,"*":2, "/":2, "(":0}
        st = [] #operators
        s = ""   #operands
        for i in exp[::-1]:
            if i in precedence.keys():
                x = st.pop()
                y = st.pop()
                st.append("("+x+i+y+")")
            else:
                st.append(i)
        return st
                
            
print(prefixToInfix("*-A/BC-/AKL"))
