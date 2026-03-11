print("ADIVINA EL NUMERO")

vida = 0
while vida < 3:
    numero1 = int(input("Elige el numero: "))
    if numero1 == 7:
        print("GANASTE!")
        vida = vida + 1
        break
    elif numero1 <7:
        print("Muy bajo!")
        vida = vida + 1
    else:
        print("Muy alto!")
        vida = vida + 1

if vida == 3:
    print("PERDISTE!")
