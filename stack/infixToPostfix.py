def InfixtoPostfix(self,exp):
        precedence = {"^":3, "+":1, "-":1 ,"*":2, "/":2, "(":0}
        st = [] #operators
        s = ""   #operands
        for i in exp:
            if i == "(":
                st.append(i)
            elif len(st)!=0 and i==")":
                while  st[-1] != "(":
                    s+=st.pop()
                st.pop()
                
            elif i in precedence.keys() :
                if len(st) == 0:
                    st.append(i)
                elif precedence[st[-1]] < precedence[i]:
                    st.append(i)
#               elif i =="^" and st[-1]=="^":
#                   st.append(i)
                else:
                    while len(st)!=0 and precedence[i]<=precedence[st[-1]]:
                        x=st.pop()
                        s +=x
                    st.append(i)
            
                    
            else:
                s+=i
        if len(st)!=0:
            while len(st)!=0:
                s+=st.pop()
             
        return s
