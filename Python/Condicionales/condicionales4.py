Name = "Luis"
Name2 = "luis"

if  Name == Name2:
    print("Los nombres son iguales.")
else:
    print("Los nombres son distintos.")

A = "c"

if A in ["a", "A", "b", "N"]:
    print("El elemento si existe en la lista.")
else:
    print("El elemento NO existe en la lista.")

# lower() transforma el texto en minúsculas.
# upper() transforma el texto en mayúsculas.
# title() transforma la primera letra del texto en mayúscula.

Name3 = input("Tu nombre: ")
if Name3 == Name3.lower():
    print("Hola, " + Name3.title())
else:
    print("Tu nombre no esta escroto en minúsculas.")

list = ["LUIS", "GOKU", "Antonio", "vegeta"]

if Name3.upper() in list:
    print("Estas en la lista.")
else:
    print("No estas en la lista, chavo.")