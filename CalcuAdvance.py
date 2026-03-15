def sumar(n1, n2):
    print(n1 + n2)

def restar(n1, n2):
    print(n1 - n2)

def multiplicar(n1, n2):
    print(n1 * n2)

print("=" * 30)
print("       |Calculadora|")
print("=" * 30)
while True:
    print("-" * 30)
    operacion = int(input("1.Sumar, 2.Restar, 3.Multiplicar, 4.Salir: "))
    print("-" * 30)
    if operacion == 4:
        break
    numero1 = int(input("Numero1: "))
    numero2 = int(input("Numero2: "))
    if operacion == 1:
        sumar(numero1, numero2)
    elif operacion == 2:
        restar(numero1, numero2)
    else:
        multiplicar(numero1, numero2)
