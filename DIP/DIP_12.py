"""
*** BaSuZ3 ***
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given the root of a binary tree. Invert the binary tree in place. That is,
all left children should become right children, and all right children should become left children.

Example:
    a
   / \
  b   c
 / \  /
d   e f

The inverted version of this tree is as follows:
  a
 / \
 c  b
 \  / \
  f e  d

Here is the function signature:
class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print self.value,
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invert(node):
  # Fill this in.

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print "\n"
invert(root)
root.preorder()
# a c f b e d
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