"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

Input: "tracecars"
Output: racecar
"""

# Solución / Solution - class, function, etc.
def LongestPalindromic(s):
    S = s.lower()
    size = len(s)
    S_Long = ""
    #for l in S[:size//2]:
    for i in range(size - 1):
        #mitad = size//2 + 1 if size%2 == 0 else size//2 + 2
        S_sub = S[i:]
        tam = len(S_sub) # tamaño sub-string
        if tam < len(S_Long):
            break
            #print("Es menor, corte")
        #print("sub: " + S_sub, ", i = " + str(i) + ", tam = " + str(tam) + ", len(long) = " + str(len(S_Long)))
        for j in range(tam - 1):
            S_i = S_sub[:tam - j] # recorta la palabra segun j
            #print(S_i + ", j = " + str(j))
            if S_i == S_i[::-1]: # revisa si es palindromo
                #print("palindromo: " + S_i + " == " + S_i[::-1])
                if len(S_Long) < len(S_i):
                    S_Long = S_i
                break
        
    return S_Long


s = "tracecars"
sol = LongestPalindromic(s)
print("Solución: " + sol)