"""
*** BaSuZ3 ***
Plantilla / Template
Normally I will place the description of the problem to be solved here.

Bonus: Here some kind of bonus to encourage good practices or things like that.
"""

# Solución / Solution - class, function, etc.
def add_uwus(texto, uwu = 'uwu'):
    """
    Here is the description of the function (what is shown when you place the mouse over it), for example:\n
    add_uwus(texto, uwu = 'uwu')\n
    [texto -> string | uwu -> string | return -> string]

    Take a string "text" and add the parameter "uwu" at the beginning and at the end.
    By default the value of the variable "uwu" is 'uwu'.
    
    >>> add_uwus('Dr. Aven')
    > 'uwu Dr. Aven uwu'
    """
    return "uwu " + texto + " uwu"



dr_aven = "BaSuZ3"
uwus = add_uwus(dr_aven)
print(uwus)