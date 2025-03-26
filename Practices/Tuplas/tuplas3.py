tupla1 = ("Luis", "Hernández", "Mendoza", 29, 5510947138)
tupla2 = (1, 7, 3, 7, 8, 90, 7, 1, 7)

# Guardar los elementos de una tupla en variables independientes.
nombre, apellido, apellido2, edad, tel = tupla1

print(nombre)
print(apellido)
print(apellido2)
print(edad)
print(tel)

print("\nGuardar tupla en una lista.")
lista_tupla = list(tupla1)
print(lista_tupla)

print("\nEncontrar un elemento en la tupla.")
print("Hernández" in tupla1)

print("\nBuscar elementos en una tupla.")
print(tupla2.count(7))

print("\nContar elementos dentro de la tupla.")
if tupla2.count(7) > 2:
    print(f"El número 7 se repite {tupla2.count(7)} veces.")

print("\nEncontrar un elemento en la tupla usando ciclo FOR.")
for dato in tupla1:
    print(dato)
    if dato == "Mendoza":
        print(f"Hola, {dato}.")