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

# Solución / Solution - class, function, etc.
def agrega_uwus(texto, uwu = 'uwu'):
    """
    Acá se coloca la descripción de la función (lo que se muestra cuando colocas el maus por encima de ella), por ejemplo:\n
    agrega_uwus(texto, uwu = 'uwu')\n
    [texto -> string | uwu -> string | return -> string]

    Toma un string "texto" y le añade el parámetro "uwu" al inicio y al final.
    Por defecto el valor de la variable "uwu" es 'uwu'.
    
    >>> agrega_uwus('Dr. Aven')
    > 'uwu Dr. Aven uwu'
    """
    return "uwu " + texto + " uwu"



dr_aven = "BaSuZ3"
uwus = agrega_uwus(dr_aven)
print(uwus)