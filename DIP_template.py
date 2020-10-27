"""
*** BaSuZ3 ***
Plantilla / Template
Normalmente colocare aquí debería ir la descripción del problema a resolver.

Bonus: Acá algún tipo de bonus para incentivar buenas practicas o cosas por el estilo.
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