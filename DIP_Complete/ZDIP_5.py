"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]

Input: A = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] , target = 9
Output: [-1, -1]
"""

# solution
def getRange(A, x):
    pivot = 0
    mini = -1
    maxi = -1
    for i in range(len(A)):
        if x == A[i] and pivot == 0:
            pivot = 1
            mini = maxi = i
        elif x == A[i]:
            maxi = i
    S = [mini, maxi]
    return S


A = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] # array
x = 9 # target
sol = getRange(A, x)
print("Solución: " + str(sol))