# ordenacion_matriz.py

def ordenar_fila(matriz, indice_fila):
    """
    Ordena una fila específica de una matriz en orden ascendente.

    Args:
        matriz (list): La matriz bidimensional.
        indice_fila (int): El índice de la fila que se desea ordenar.
    """
    # Verificamos que el índice de la fila sea válido
    if 0 <= indice_fila < len(matriz):
        # Accedemos a la fila y la ordenamos en su lugar con el método sort()
        # sort() usa un algoritmo de ordenación Timsort, que es muy eficiente en Python
        matriz[indice_fila].sort()
        print(f"La fila {indice_fila} ha sido ordenada.")
    else:
        # Si el índice no es válido, mostramos un mensaje de error
        print(f"Error: El índice de fila {indice_fila} no es válido.")


# Definimos la matriz bidimensional original con una fila desordenada
matriz_numeros_desordenada = [
    [10, 20, 30],
    [9, 1, 5],  # Esta es la fila que vamos a ordenar (índice 1)
    [40, 50, 60]
]

# Mostramos la matriz original
print("--- Matriz Original ---")
for fila in matriz_numeros_desordenada:
    print(fila)

# Definimos el índice de la fila que queremos ordenar
fila_a_ordenar = 1

# Llamamos a la función para ordenar la fila específica
ordenar_fila(matriz_numeros_desordenada, fila_a_ordenar)

# Mostramos la matriz con la fila ya ordenada
print("\n--- Matriz con la fila ordenada ---")
for fila in matriz_numeros_desordenada:
    print(fila)

