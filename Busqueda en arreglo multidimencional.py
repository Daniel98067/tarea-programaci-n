# busqueda_matriz.py

def buscar_valor(matriz, valor_a_buscar):
    """
    Busca un valor específico en una matriz bidimensional.

    Args:
        matriz (list): La matriz bidimensional donde se realizará la búsqueda.
        valor_a_buscar (int/float): El valor que se desea encontrar.

    Returns:
        tuple or None: Una tupla con la posición (fila, columna) del valor si se encuentra,
                       de lo contrario, devuelve None.
    """
    # Recorremos cada fila de la matriz
    for fila_indice, fila in enumerate(matriz):
        # Recorremos cada elemento de la fila
        for col_indice, elemento in enumerate(fila):
            # Comparamos si el elemento actual es el valor que buscamos
            if elemento == valor_a_buscar:
                # Si lo encontramos, devolvemos su posición como una tupla (fila, columna)
                return (fila_indice, col_indice)

    # Si el bucle termina sin encontrar el valor, devolvemos None
    return None


# Definimos la matriz bidimensional
matriz_numeros = [
    [1, 5, 9],
    [12, 16, 20],
    [23, 27, 31]
]

# Definimos el valor que queremos buscar
valor = 16

# Llamamos a la función para buscar el valor y guardamos el resultado
posicion = buscar_valor(matriz_numeros, valor)

# Mostramos un mensaje basado en el resultado de la búsqueda
if posicion:
    # Si 'posicion' no es None, significa que se encontró el valor
    fila, columna = posicion
    print(f"El valor {valor} fue encontrado en la posición ({fila}, {columna}).")
else:
    # Si 'posicion' es None, el valor no está en la matriz
    print(f"El valor {valor} no se encuentra en la matriz.")

# Ejemplo de búsqueda de un valor que no existe
valor_no_existente = 100
posicion_no_existente = buscar_valor(matriz_numeros, valor_no_existente)

print("\n--- Búsqueda de un valor no existente ---")
if posicion_no_existente:
    fila, columna = posicion_no_existente
    print(f"El valor {valor_no_existente} fue encontrado en la posición ({fila}, {columna}).")
else:
    print(f"El valor {valor_no_existente} no se encuentra en la matriz.")
