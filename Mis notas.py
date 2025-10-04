# Escritura de Archivo de Texto
# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: Aprender Python es divertido.\n")
    file.write("Nota 2: Practicar con archivos mejora las habilidades.\n")
    file.write("Nota 3: La perseverancia es clave para el éxito.\n")
# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el archivo línea por línea usando readline()
    line = file.readline()  # Leemos la primera línea
    while line:
        # Mostramos la línea leída en la consola
        print(line, end='')  # end='' evita añadir una línea extra
        # Leemos la siguiente línea
        line = file.readline()
# No es necesario cerrar el archivo explícitamente cuando usamos 'with',
# ya que este contexto se encarga de cerrarlo automáticamente.
