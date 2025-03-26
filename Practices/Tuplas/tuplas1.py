# Las tuplas son listas inmutables; significa que no se pueden modificar con append, extend o remove.
# Utilidad: Más rápidas, formatean Strings y se pueden utilizar con claves para diccionarios.

frutas = tuple(("Melón", "Papaya", "Sandía", "Plátano"))
# Imprimir tupla.
print(frutas)

# Imprimir una posición específica de la tupla.
print(frutas[1])

# Consultar la longitud de la tupla.
print(len(frutas))

# Consultar el tipo de la variable.
print(type(frutas))