"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""

# Solución / Solution - class, function, etc.
def isValid(s):
    check = [] # check ()
    size = len(s)
    if size%2 != 0:
        return False
    for l in s:
        if len(check) == 0:
            check.append(l)
            #print("agregar: " + l + ", tam = " + str(len(check)))
        else:
            ultimo = len(check) - 1
            if l == "(":
                check.append(l)
            elif l == "{":
                check.append(l)
            elif l == "[":
                check.append(l)
            elif l == ")":
                if check[ultimo] == "(":
                    check.pop(ultimo)
                else:
                    return False
            elif l == "}":
                if check[ultimo] == "{":
                    check.pop(ultimo)
                else:
                    return False
            elif l == "]":
                if check[ultimo] == "[":
                    check.pop(ultimo)
                else:
                    return False
    #print(check)
    return True

s = "({[)]"
sol = isValid(s)
print(sol)