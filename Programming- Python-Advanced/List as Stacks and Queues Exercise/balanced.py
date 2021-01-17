parentheses = input()
s = []
for char in range(len(parentheses)):
    if parentheses[char] == "(" or parentheses[char] == "[" or parentheses[char] == "{":
        s.append(parentheses[char])
    if s:
        if parentheses[char] == ')' and s[-1] == '(':
            s.pop()
        elif parentheses[char] == ']' and s[-1] == '[':
            s.pop()
        elif parentheses[char] == '}' and s[-1] == '{':
            s.pop()

    else:
        s.append(parentheses[char])
        break

if len(s) != 0:
    print('NO')
else:
    print('YES')