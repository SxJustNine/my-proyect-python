"VAMOS A USAR LA LOGICA PARA HACER DATOS 1.intento"

def nombre():
    nombre = input("Cual es tu nombre: ")
    return nombre

def edad():
    edad = int(input("Cual es tu edad: "))
    if edad >= 18:
        print("Bienvenido")
    elif edad < 18:
        print("No puedes acceder!")
        return edad
    quit()

def localidad():
    localidad = input("Cual es tu localidad: ")
    return localidad

# DATOS
mi_nombre = nombre()
mi_edad = edad()
mi_localidad = localidad()
print("=" * 15)

print("Nombre:", mi_nombre)
print("Edad:", mi_edad)
print("Localidad", mi_localidad)
