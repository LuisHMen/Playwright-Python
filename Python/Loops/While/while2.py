# Adivina el número con while.

number = 7
flag = True

while flag == True:
    n = int(input("Número entre 1 - 10: "))

    if n > 10 or n < 1:
        print("Te dije que un número entre 1 y 10.")
    else:
        if n == number:
            print(f"¡Adivinaste el número! {number}")
            flag = False
        elif n > number:
            print(f"El número {n} es mayor.")
        elif n < number:
            print(f"El número {n} es menor.")