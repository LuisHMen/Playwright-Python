# Un return puede regresar múltiples valores.

def operations(a, b):
    sum = a + b
    subtract = a - b
    multiply = a * b
    return sum, subtract, multiply

print(f"Todos los resultados: {operations(10, 7)}")

sum = operations(10, 7)[0]
subtract = operations(10, 7)[1]
multiply = operations(10, 7)[2]

print(f"Suma {sum}")
print(f"Resta {subtract}")
print(f"Multiplicación {multiply}")