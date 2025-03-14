
temperaturas = [
    # Santo Domingo	
    [
        # Semana 1
        [25, 26, 27, 28, 29, 30, 31],  # Lunes a Domingo
        # Semana 2
        [24, 25, 26, 27, 28, 29, 30],
        # Semana 3
        [23, 24, 25, 26, 27, 28, 29],
        # Semana 4
        [22, 23, 24, 25, 26, 27, 28]
    ],
    # Cuenca 
    [
        # Semana 1
        [20, 21, 22, 23, 24, 25, 26],
        # Semana 2
        [19, 20, 21, 22, 23, 24, 25],
        # Semana 3
        [18, 19, 20, 21, 22, 23, 24],
        # Semana 4
        [17, 18, 19, 20, 21, 22, 23]
    ],
    # Quito 
    [
        # Semana 1
        [30, 31, 32, 33, 34, 35, 36],
        # Semana 2
        [29, 30, 31, 32, 33, 34, 35],
        # Semana 3
        [28, 29, 30, 31, 32, 33, 34],
        # Semana 4
        [27, 28, 29, 30, 31, 32, 33]
    ]
]

# Nombres de las ciudades
ciudades = ["Santo Domingo", "Cuenca", "Quito"]

for i in range(len(ciudades)):  # Iterar sobre ciudades
    print(f"Promedios de temperatura para {ciudades[i]}:")
    for j in range(len(temperaturas[i])):  # Iterar sobre semanas
        semana = temperaturas[i][j]
        promedio = sum(semana) / len(semana)
        print(f"  Semana {j + 1}: {promedio:.2f}°C")
    print() 
