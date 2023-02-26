def reverseWords(S):
        string = S
        st = []
        s = ""
        for i in string[::-1]:


            if i == " ":
                while len(st)!=0:
                    s += st.pop()
                s+=" "

            else:
                st.append(i)
        if len(st)!=0:
            while len(st)!=0:
                s+= st.pop()

        return s
print(reverseWords("i like this program very much"))
