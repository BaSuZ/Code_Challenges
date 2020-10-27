"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Apple:

Given an integer k and a binary search tree, find the floor (less than or equal to)
of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.
class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)
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