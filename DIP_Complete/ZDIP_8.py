"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5, 
return true since 4 + 1 = 5.

Try to do it in a single pass of the list.
"""

# Solución / Solution - class, function, etc.
def TwoSum(A, k):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if k == A[i] + A[j]:
                return True
    return False


A = [4, 7, 1 , -3, 2]
k = 5
sol = TwoSum(A, k)
print(sol)