nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
calificacion_1 = float(input("Ingrese la primera nota: "))
calificacion_2 = float(input("Ingrese la segunda nota: "))
calificacion_3 = float(input("Ingrese la tercera nota: "))

promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

promrnd = round(promedio, 2)

if promedio >=71:
    print("Tu promedio es:", promrnd, "y has aprobado")
else: 
    print("Tu promedio es:", promrnd, "y no has aprobado")