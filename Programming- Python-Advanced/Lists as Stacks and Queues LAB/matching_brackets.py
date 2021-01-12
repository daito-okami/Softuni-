expr = input()


s = []

for i in range(len(expr)):
    ch = expr[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        j = s.pop()
        print(expr[j:i + 1])
