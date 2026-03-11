import random

print("PIEDRA PAPEL TIJERAS")
opciones = ("Piedra", "Papel", "Tijera")

vida = 0
while vida <3:
  computadora = random.choice(opciones)
  print("computadora eligio:", computadora)
  elegir = input("elige: ").capitalize()
  if elegir == "Piedra" and computadora == "Tijera" or elegir == "Papel" and computadora == "Piedra" or elegir == "Tijera" and computadora == "Papel":
    print("Ganaste!")
    vida = vida + 1
  elif elegir == computadora:
    print("EMPATE!")
    vida = vida + 1
  else:
    print("PERDISTE!")
    vida = vida + 1
