import numpy as np

def temperatura_promedio(temperaturas):
  """
  Calcula la temperatura promedio de una o varias ciudades a lo largo de un período.

  Args:
    temperaturas (np.array): Un array de NumPy con las temperaturas.
                             La forma esperada es (ciudades, semanas).

  Returns:
    np.array: Un array de NumPy con la temperatura promedio por ciudad.
  """
  return np.mean(temperaturas, axis=1)

# Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas
# Fila 0: Quito
# Fila 1: Guayaquil
# Fila 2: Cuenca
# Columnas: Semana 1, Semana 2, Semana 3, Semana 4
datos_ciudades = np.array([
    [19, 24, 26, 16],  # Quito
    [33, 34, 32, 27],  # Guayaquil
    [10, 15, 14, 11]   # Cuenca
])

# Nombres de las ciudades para una mejor visualización
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Calcular la temperatura promedio utilizando la función
promedios = temperatura_promedio(datos_ciudades)

# Mostrar los resultados
for i, ciudad in enumerate(ciudades):
  print(f"La temperatura promedio de {ciudad} es: {promedios[i]:.2f}°C")