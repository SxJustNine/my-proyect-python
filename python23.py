pelicula = [
    {"Nombre": "Sabuesos", "Año": 2023, "Director": "Kim Joo-kwan"},
    {"Nombre": "Megamente", "Año": 2010, "Director": "DreamWorks"},
    {"Nombre": "BreakingBad", "Año": 2008, "Director": "Vince Gilligan"}
]
pelicula.append({"Nombre": "Heroe debil", "Año": 2022, "Director": "Yoo Soo-min"})
print("=" * 35)
print("PELICULAS".center(35))
print("=" * 35)

for Peliculas in pelicula:
    print(f"Nombre: {Peliculas['Nombre']} | Año: {Peliculas['Año']} | {Peliculas['Director']}")

print("=" * 35)