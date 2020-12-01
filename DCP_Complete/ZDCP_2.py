"""
*** BaSuZ3 ***
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# Solución / Solution - class, function, etc.
def producto_sin_index(A):
    """
    [A -> integers array | return -> integers array]

    Dado una lista de enteros "A", retorna una lista de enteros del mismo tamaño, en donde cada elemento en la posición "i" representa la multiplicación de todos los otros elementos de la lista de "A", sin incluir el elemento "i".
    
    >>> A = [1, 2, 3, 4, 5]
    >>> all_product_without_index(A)
    > [120, 60, 40, 30, 24]

    Complejidad.
        Tiempo de ejecución:
            = 1 + (n + 1 + 1) * (n + 1+ 3)
            = 1 + n^2 + 6n + 8
            -> *** O(n^2) ***
        Espacio:
            = n + 1
            -> *** O(n) ***
    """
    productos = [] # 1 *** n
    for i in range(len(A)): # n
        producto = 1 # 1 *** 1
        for j in range(len(A)): # n
            if i != j: # 1
                producto = producto * A[j] # 3
        productos.append(producto) # 1
    return productos



A = [1, 2, 3, 4, 5]
sol = producto_sin_index(A)
print(sol)