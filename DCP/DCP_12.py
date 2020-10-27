"""
*** BaSuZ3 ***
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
•	1, 1, 1, 1
•	2, 1, 1
•	1, 2, 1
•	1, 1, 2
•	2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from
a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
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