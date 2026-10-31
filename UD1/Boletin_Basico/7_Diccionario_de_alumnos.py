from pip._internal import self_outdated_check

alumnos = {}

while True:

    print("----MENU----")
    print("1...Añadir un alumno con nota")
    print("2...Buscar nota alumno")
    print("3...Media de notas")
    print("4...Nota mas alta")
    print("5...SALIR")
    opcion = int(input("Di una opcion"))

    if opcion == 1:
        nombre = input("Dime el nombre del alumno")
        nota = float(input("Dime la nota"))
        alumnos[nombre] = nota
    elif opcion == 2:
        nombre_busca = input("Dime el nombre que buscas")

        if nombre_busca in alumnos:
            print(f"Nota de {nombre_busca}: {alumnos[nombre_busca]}")

    elif opcion == 3:
        media = sum(alumnos.values()) / len(alumnos)
        print(f"La media es de {media} puntos")

    elif opcion == 4:
        nota_max = max(alumnos.values())
        print(f"La nota mas alta es {nota_max} puntos")

    elif opcion == 5:
        print("ADIOOOOOS")
        break