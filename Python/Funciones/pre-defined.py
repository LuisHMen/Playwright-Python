# Funciones ya predefinidas en Python.

# División con residuo.
# Divide el número de veces posible y te muestra el número restante.
def division(a, b):
    return divmod(a, b)
# 7 x 11 son 77. 77 - 80 = 3. Por eso el resultado.
divi = division(80, 7)
print(f"Divisón: {divi}")

# Identificar el mayor.
def mayorN(a, b, c, d, e):
    mayor = max(a, b, c, d, e)
    return mayor

print(f"Mayor: {mayorN(700, 81, 12, 45, 100)}")

# Identificar el menor.
def menorN(a, b, c, d, e):
    menor = min(a, b, c, d, e)
    return menor

print(f"Menor: {menorN(700, 81, 12, 45, 100)}")