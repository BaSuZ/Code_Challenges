"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
Comment all: (alt + shift + A)
# Otro comentario: (ctrl + k + c)
"""

class Nodo():
    def __init__(self, x):
        self.valor = x
        self.next = None

class Sol():
    def SumarNum(self, l1, l2,):
        x = l1.valor + l2.valor
        c = 0
        if x > 9:
            x = x - 10
            c = 1
        #print("x = " + str(x) + ", c = " + str(c))
        lSol = Nodo(x)
        lAux = lSol
        l1 = l1.next
        l2 = l2.next
        while l1 != None or c == 1:
            if l1 != None and l2 != None:
                x = l1.valor + l2.valor + c
            else:
                x = c
            c = 0
            if x > 9:
                x = x - 10
                c = 1
            #print("x = " + str(x) + ", c = " + str(c))
            l1 = l1.next
            l2 = l2.next
            lAux.next = Nodo(x)
            lAux = lAux.next
        return lSol

l1 = Nodo(2)
l1.next = Nodo(4)
l1.next.next = Nodo(3)

l2 = Nodo(5)
l2.next = Nodo(6)
l2.next.next = Nodo(4)

result = Sol().SumarNum(l1 ,l2)

while result:
    print("valor = " + str(result.valor))
    result = result.next