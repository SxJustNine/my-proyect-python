print("CALCULADORA")

operacion = int(input("1-sumar, 2-restar, 3-multiplicar:  "))
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
if operacion == 1:
    print(numero1 + numero2)
elif operacion == 2:
    print(numero1 - numero2)
else:
    print(numero1 * numero2)
