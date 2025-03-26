# Imprimir un arreglo con for.

frutas = ["Melón", "Papaya", "Sandía", "Plátano", "Pera"]
for f in frutas:
    print(f)

# Encontrar un elemento dentro del arreglo con for.
for fav in frutas:
    if(fav == "Sandía"):
        print("Fruta favorita: " + fav)
    else:
        print("Otras frutas: " + fav)

# Break: Detener ejecución del bucle.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0

for num in numbers:
    result += num
    if num == 7: # La suma se detiene cuando llega al 7.
        break
    print("Suma total: " + str(result))

# Continue: Omitir poisicones de la lista.
x = 0
for num in numbers:
    if num == 7: # Este es el valor que omite en la suma.
        continue
    x += num
    print("Suma: " + str(x))