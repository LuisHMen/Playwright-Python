# CAPITALIZE
# Función que se encarga de transformar la primera letra
# de una palabra en mayúscula (si no es máyuscula).
print("CAPITALIZE")
Word = "palabra demo"
Word = Word.capitalize()

print(Word)

# CASE FOLD
# Función que transforma todas las letras máyusculas a minúsculas.
print("\nCASE FOLD")
Sentence = "Hello, Luis Hernández M."
Sentence = Sentence.casefold()

print(Sentence)

# CENTER
# Función para mover caracteres la cantidad de pixeles que indiques hacia el centro.
print("\nCENTER")
Caracteres = "Hola, aquí estoy."
Centrar = Caracteres.center(50)

print(Centrar)

# COUNT
# Cuenta las veces que se repite un valor/palabra dentro de una cadena.
# La función es sensible a minúsculas y mayúsculas.
print("\nCOUNT")
Chain = "Las manzanas rojas saben más ricas que las manzanas verdes."
Counter = Chain.count("manzanas")

print("Palabra repetida: " + str(Counter))

# Counter pero ahora con un arreglo para limitar la cantidad de caracteres
# que la función va a recorrer para encontrar los valores.
Chain2 = "7 Probando si la función 7 cuenta los 3 números 7 que están aquí."
Counter2 = Chain2.count("7", 0, 30)

print("Número repetido: " + str(Counter2))

# ENDS WITH
# Verifica que el último valor de la cadena sea igual al que indiques.
# Esta función trabaja con boolean.
# Si correcto = True, Si incorrecto = False.
print("\nENDS WITH")
Sentence = "Esta función verifica que este sea el último valor."
Find = Sentence.endswith("último valor.")

print(Find)
if Find == True: print("Valor encontrado.")
else: print("No encontrado.")

# FIND
# Localizador de caracteres. 
# Indica en que posición de la cadena se encuentra el caracter buscado.
# Si el valor no existe, entonces la función devolverá un valor negativo.
print("\nFIND")
Sentence2 = "La función me indicará en que posición se encuentra ESTA palabra."
Find = Sentence2.find("ESTA", 0, 100)

print("El valor está en la posición: " + str(Find))