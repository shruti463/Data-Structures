def sorted(s):
    st = []
    while len(s)!=0:
        x =s[-1]
        s.pop()
        while len(st)!=0 and x<st[-1]:
            s.append(st[-1])
            st.pop()
        st.append(x)
    return st
print(sorted([11,2,32,3,41]))
