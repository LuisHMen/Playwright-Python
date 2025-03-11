# Calcular el pago de horas trabajadas.

Nombre = input("Nombre: ")
Horas = float(input("¿Cuántas horas trabajaste?: "))
PagoxHora = float(input("Monto que cobras por hora: "))

PagoTotal = Horas * PagoxHora

print(Nombre + " el monto a pagar es: " + str(PagoTotal))