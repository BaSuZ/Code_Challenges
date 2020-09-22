"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list using constant space.
"""

# solution
def sortNums(A):
    MID = 2
    n = len(A) - 1
    i = 0
    j = 0
    while j < n:
        if A[j] < MID:
            [A[i], A[j]] = [A[j], A[i]]
            i +=1
            j +=1
        elif A[j] > MID:
            [A[n], A[j]] = [A[j], A[n]]
            n -=1
        else:
            j +=1


A = [3, 3, 2, 1, 3, 2, 1]
sortNums(A)
print(A)