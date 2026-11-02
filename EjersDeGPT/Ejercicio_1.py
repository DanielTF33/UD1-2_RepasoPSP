alumnos = []

def agregar_alumno(nombre, nota):

    diccionario = {"nombre": nombre, "nota": nota}

    alumnos.append(diccionario)

def calcular_media():
    if len(alumnos) == 0:
        return 0

    suma = 0

    for alumno in alumnos:
        suma = suma + alumno["nota"]

    return  suma / len(alumnos)


def mostrar_aprobados():

    for alumno in alumnos:
        if alumno["nota"] >= 5:
            print(f"Nombre: {alumno["nombre"]} + Nota: {alumno["nota"]}")


if __name__ == '__main__':

    agregar_alumno("Ana", 8)
    agregar_alumno("Luis", 4)
    agregar_alumno("Marta", 9)
    agregar_alumno("Pedro", 3)


    print(f"Media: {calcular_media()}")

    mostrar_aprobados()
