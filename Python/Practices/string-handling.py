# STRING CUT
# Tomar una muestra específica del texto.
print("STRING CUT")
Text = "Dependiendo de las posiciones indicadas, la función toma una parte del texto para imprimirla."
print("Muestra: " + Text[19:60])
print("Muestra sin inicio: " + Text[:30])
print("Muestra sin fin: " + Text[40:])

# MANIPULATE TEXT
print("\nMANIPULATE TEXT")
Text1 = "     Manipulando este texto."
# Mayúsculas
Manipulado = Text1.upper()
print("Mayúsculas: " + Manipulado)

# Minúsculas
Manipulado = Text1.lower()
print("Minúsculas: " + Manipulado)

# Quitar espacios innecesarios
Manipulado = Text1.strip()
print("Sin espacios: " + Manipulado)

# Reemplazar palabras
Manipulado = Text1.replace("este", "-el-")
print("Reemplar por -el-: " + Manipulado)

# DIAGONALES INVERTIDAS (ESCAPE)
print("\nDIAGONALES INVERTIDAS (ESCAPE)")
Comillas = "Texto con \"comillas\"."
print(Comillas)

# TABULADORES Y SALTO DE LÍNEA
print("\nTABULADORES Y SALTO DE LÍNEA.")
Texto = "\tTexto con 1 tab. \n\t\tSalto de línea y 2 tabs. \n\t\t\t\rLa R (retorno) anula los tabs."
print(Texto)