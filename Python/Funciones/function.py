# Estructura de una función.
# def func(parameter1, parameter2):
    # Function code <-- Identación.
    # return

# Llamar a la función.
# func(argument1, argument2)

# Guardar el retorno de la función.
# var = func(argument1, argument2)

# Función.
def calc_perc(value, percentage):
    # Function code <-- Identación.
    percentage = percentage / 100
    result = value * percentage
    return result

# Solicitar valores para la función.
value = float(input("Valor: "))
percentage = float(input("Porcentaje: "))

if value > 0 and percentage > 0:
    # Guardando el retorno de la función en result.
    result = calc_perc(value, percentage)
    print(f"{result} equivale al {percentage}% de {value}.")
else:
    print("Únicamente valores mayores a 0.")