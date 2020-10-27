"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory.
"""

# Solución / Solution - class, function, etc.
def SingleNumber(A):
    repeat = False
    A.sort()
    i = 0
    while i < len(A):
    #for i in range(len(A) - 1):
        visto = 0
        if i == len(A) - 1:
            if A[i - 1] != A[i]:
                return A[i]
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                visto = 1
                continue
            elif visto == 1:
                i = j - 1
                break
            else:
                return A[i]
        i += 1
    return repeat


A = [4, 3, 2, 4, 1, 3, 2, 1, 5, 6, 6]
sol = SingleNumber(A)
print(sol)