"""
*** BaSuZ3 ***
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# solution
def sumaConArreglo(A, k):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if k == A[i] + A[j]:
                return True
    return False


A = [10, 15, 3, 7]
k = 17
sol = sumaConArreglo(A, k)
print(sol)