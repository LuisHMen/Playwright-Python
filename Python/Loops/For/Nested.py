# Tablas de multiplicar con FOR ANIDADO.

# for a in range (6, 9): # Números a multiplicar.
#     for b in range (1, 11): # Veces que se multiplica el número.
#         print(f"{a} x {b} = {a*b}")

# Recorrer una cadena de caracteres.
# Practicamente se puede recorrer todo, pero en este caso será una cadena de caracteres.
palabra = "Texto de prueba."
for p in palabra:
    print(f"Poisición -> {p}")

# Contar elementos repetidos.
name = "Mike Ross Pearson Specter."
contador = 0

for letra in name:
    if(letra == "e"):
        contador += 1
print(f"Letra repetida {contador} veces.")

