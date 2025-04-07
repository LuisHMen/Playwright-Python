# Ciclo while.
x = 0
while x < 5:
    print("Número: " + str(x))
    x += 1

# Menú constante.
option = 0
while option != 3:
    a = 0
    b = 0
    print(f"Opción 1: Suma.")
    print(f"Opción 2: Resta.")
    print(f"Opción 3: Salir.")

    option = int(input("Seleccione una opción: "))

    if option == 1:
        a = float(input("Primer valor: "))
        b = float(input("Segundo valor: "))
        suma = a + b
        print("Suma: " + str(suma) + "\n")
    elif option == 2:
        a = float(input("Primer valor: "))
        b = float(input("Segundo valor: "))
        resta = a - b
        print(f"Resta: {resta} \n")
    elif option == 3:
        print(f"Hasta luego.")
    else:
        print("No seleccionaste una opción valida.\n")