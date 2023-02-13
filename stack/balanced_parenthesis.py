import stack as node

def parenthesis(strr):
    for i in strr:
        if i in ["(","[","{"]:
            s.push(i)
        else:
            if s.isEmpty():
                return False
            current = s.pop()
            if current == "[" and i != "]":
                return False
            if current == "{" and i != "}":
                return False
            if current == "(" and i != ")":
                return False
    if s.isEmpty():
        return True
    return False


s = node.stack()
strr="[{()}[]]"
print(parenthesis(strr))



