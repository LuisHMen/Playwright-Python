# OR (o) indica que se tiene que cumplir UNA de todas las condiciones.

a = 10
b = 20
c = 35

if a > b or a > c:
    print("El mayor es A.")

elif b > a or b > c:
    print("El mayor es B.")

elif c > a or c > b:
    print("El mayor es C.")