# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el descuento a aplicar a un monto total.

  Args:
    monto_total: El monto total de la compra.
    porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto, 10%).

  Returns:
    El monto del descuento calculado.
  """
  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# --- Llamadas a la función y resultados ---

# Ejemplo 1: Aplicando el descuento predeterminado (10%)
monto_compra_1 = 250
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

print(f"Compra 1:")
print(f"Monto total: ${monto_compra_1:.2f}")
print(f"Porcentaje de descuento: 10%")
print(f"Monto del descuento: ${descuento_1:.2f}")
print(f"Monto final a pagar: ${monto_final_1:.2f}")
print("-" * 30)

# Ejemplo 2: Aplicando un descuento personalizado (20%)
monto_compra_2 = 500
porcentaje_personalizado = 20
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_personalizado)
monto_final_2 = monto_compra_2 - descuento_2

print(f"Compra 2:")
print(f"Monto total: ${monto_compra_2:.2f}")
print(f"Porcentaje de descuento: {porcentaje_personalizado}%")
print(f"Monto del descuento: ${descuento_2:.2f}")
print(f"Monto final a pagar: ${monto_final_2:.2f}")