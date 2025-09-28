# 1. Crear un diccionario
informacion_personal = {
    "nombre": "Daniel Arévalo",
    "edad": 18,
    "ciudad": "Quito",
    "profesion": "Ingeniera de software"
}

# 2. Acceder y modificar valores
informacion_personal["ciudad"] = "Milagro"

# 3. Agregar una nueva clave-valor
informacion_personal["profesion"] = "Criminalística"

# 4. Verificar existencia de claves y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0941792129"

# 5. Eliminar una clave
del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print(informacion_personal)