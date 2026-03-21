print("=" * 30)
print("DATOS/O FORMULARIO")
print("-" * 30)

def pedir_datos():
    while True:
            nombre = input("Nombre: ")
            if nombre .isalpha():
                break
            else:
                print("Escribi Letras")
    while True:
        try:
            edad = int(input("Edad:"))
            if edad >= 18:
                categoria = "+18"
            elif edad < 18:
                categoria = "-18"
            break
        except:
            print("Escribi un numero, no una letra")

    localidad =input("Localidad: ")
    return nombre, edad ,localidad, categoria

nombre, edad, localidad, categoria = pedir_datos()

print("=" * 30)
print("Resumen")
print("-" * 30)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} ({categoria})")
print(f"Localidad: {localidad}")
print("=" * 35)
