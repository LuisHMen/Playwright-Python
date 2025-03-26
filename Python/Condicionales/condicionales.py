# Igualdad a == b
# Diferente de a != b
# Menor que a < b
# Menor o igual que a <= b
# Mayor que a > b
# Mayor o igual que a >= b


a = 10
b = 19

if a == b:
    print("A es igual que B.")
    print(str(a) + " = " + str(b))

elif a != b:
    print("A es diferente que B.")
    print(str(a) + " != " + str(b))

elif a < b:
    print("A es menor que B.")
    print(str(a) + " < " + str(b))

elif a > b:
    print("A es mayor que B.")
    print(str(a) + " > " + str(b))

elif a <= b:
    print("A es menor o igual que B.")
    print(str(a) + " <= " + str(b))

elif a >= b:
    print("A es mayor o igual que B.")
    print(str(a) + " >= " + str(b))

else:
    print("Los valores no están condicionados.")