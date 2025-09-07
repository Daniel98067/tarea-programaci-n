# Tarea: Iteración de arreglos multidimensionales con bucles anidados

# Paso 1: Creación de la matriz 3D con datos de temperaturas
# La estructura es [ciudad][semana][día]
temperaturas = [
    # Datos para la ciudad de Quito
    [
        [15, 16, 14, 17, 18, 15, 16],  # Semana 1
        [17, 18, 17, 19, 20, 18, 19]  # Semana 2
    ],
    # Datos para la ciudad de Guayaquil
    [
        [28, 29, 30, 29, 28, 31, 30],  # Semana 1
        [27, 28, 27, 26, 29, 30, 29]  # Semana 2
    ],
    # Datos para la ciudad de Cuenca
    [
        [22, 23, 21, 24, 22, 23, 22],  # Semana 1
        [24, 25, 24, 26, 25, 24, 23]  # Semana 2
    ]
]

# Nombres de las ciudades para una mejor visualización del resultado
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Paso 2: Usar bucles anidados para calcular el promedio por ciudad y semana
print("Calculando promedios de temperatura semanales por ciudad...")

# Primer bucle: Itera sobre cada ciudad
for i, ciudad_nombre in enumerate(ciudades):

    # Segundo bucle: Itera sobre cada semana de la ciudad actual
    # 'semanas' contiene las listas de temperaturas diarias para esa semana
    for j, semana_datos in enumerate(temperaturas[i]):

        # Tercer bucle (anidado dentro del segundo): Suma las temperaturas diarias
        suma_temperaturas = 0
        for temperatura_diaria in semana_datos:
            suma_temperaturas += temperatura_diaria

        # Opcional: una forma más "pythónica" de sumar
        # suma_temperaturas = sum(semana_datos)

        # Calcular el promedio
        promedio = suma_temperaturas / len(semana_datos)

        # Mostrar el resultado en la pantalla
        print(f"El promedio de temperaturas para {ciudad_nombre} en la semana {j + 1} es: {promedio:.2f}°C")