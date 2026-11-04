alumnos = {}

while True:
    print("----MENU----")
    print("1...Anadir alumno")
    print("2...Buscar nota")
    print("3...Media")
    print("4...Nota mas alta")
    print("5...SALIR")
    opcion = int(input("DIME OPCION: "))

    if opcion == 1:
        nombre = input("Dime el nombre del alumno: ")
        nota = float(input("Dime su nota: "))

        alumnos[nombre] = nota

        print("Anadido con exito")

    if opcion == 2:

        nombre = input("Dime el nombre del alumno a buscar: ")

        if nombre in alumnos:
            print(f"Su nota es: {alumnos[nombre]}")
        else:
            print("No existe ese alumno")

    if opcion == 3:

        total = 0

        for alumno in alumnos:
            total = total + alumnos[alumno]

        print(f"La media es: {total/len(alumnos)} puntos")

    if opcion == 4:

        nota_max = max(alumnos.values())
        print(f"La nota maxima es: {nota_max} puntos")

    if opcion == 5:
        break
