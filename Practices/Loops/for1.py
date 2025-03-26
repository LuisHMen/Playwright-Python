# Imprimir un texto muchas veces.
# range(1) Límite del rango. Recuerda que un for siempre inicia en 0.
for x in range(5):
    print(f"Loop con límite 5: {x}.")

# range(1, 2) Inicio y fin del rango.
for y in range(2, 7):
    print(f"Loop con rango inicial: 2 al 7 -> {y}.")

# range(1, 2, 3) -> Inicio, fin e incrementos.
for z in range(2, 50, 10):
    print(f"Loop con incrementos de 10 en 10 -> {z}")

# Tabla del 7.
number = 7

for x in range(1, 11):
    print(f"{number} x {x} = {number*x}")