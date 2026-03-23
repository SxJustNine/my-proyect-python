#DECORACION
print("=" * 30)
print("DATOS".center(30))
print("=" * 30)

def login():
    while True:
        nombre = input("Cual es tu nombre: ")
        if nombre.isalpha():
            break
        else:
            print("Solo letras!")
    while True:
        try:
            edad = int(input("Cual es tu edad: "))
            if edad >=18:
                categoria = "+18"
            elif edad < 18:
                print("=" * 35)
                print("Eres menor de edad, No puedes pasar!".center(35))
                print("=" * 35)
                exit()
            break
        except ValueError:
            print("No letras!")
    while True:
        juego = input("Cual es tu juego favorito: ")
        if juego.replace(" ", "").isalpha():
            break
        else:
            print("Solo letras!")

    return nombre, edad, categoria, juego

nombre, edad, categoria, juego = login()
# decorativo
print("=" * 30)
print("INFORMACION".center(30))
print("=" * 30)
print(f"· Nombre: {nombre}")
print(f"· Edad: {edad} ({categoria})")
print(f"Juego Fav: {juego}")

