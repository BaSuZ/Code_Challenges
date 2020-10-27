"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

"abrkaabcdefghijjxxx" -> 10

Can you find a solution in linear time?
"""

# Solución / Solution - class, function, etc.
def LenghtOfLongerSubstring(s):
    no_Repeat = []
    pos = 0
    maximo = 0
    #cont = 0
    for l in s:
        if l not in no_Repeat:
            # No esta el elemento, se agrega
            #cont += 1
            no_Repeat.append(l)
            pos += 1
        else:
            #cont += 1
            # Si esta el elemento, empezar de nuevo
            no_Repeat = []
            if pos > maximo:
                maximo = pos
            pos = 0
    #print("maxi: " + str(cont))
    return maximo


s = "abrkaabcdefghijjxxx" # resp: 10
solucion = LenghtOfLongerSubstring(s)
print(solucion)