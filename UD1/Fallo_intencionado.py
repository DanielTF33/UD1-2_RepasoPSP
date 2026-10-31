tareas = []

def agregar_tarea(nombre, prioridad):
    tarea = {"nombre": nombre, "prioridad": prioridad, "hecha": False}
    tareas.append(tarea)

def completar_tarea(nombre):
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tarea["hecha"] = True
            return
    print("Tarea no encontrada")

def ver_tareas():
    for i, tarea in enumerate(tareas):
        estado = "✅" if tarea["hecha"] else "⬜"
        print(f"{i+1}. {estado} {tarea['nombre']} (Prioridad: {tarea['prioridad']})")

def calcular_progreso():
    if len(tareas) == 0:
        return 0
    hechas = sum(1 for t in tareas if t["hecha"])
    return hechas / len(tareas) * 100

while True:
    print("\n1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Ver tareas")
    print("4. Progreso")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la tarea: ")
        prioridad = input("Prioridad (alta/media/baja): ")
        agregar_tarea(nombre, prioridad)
    elif opcion == "2":
        nombre = input("Nombre de la tarea a completar: ")
        completar_tarea(nombre)
    elif opcion == "3":
        ver_tareas()
    elif opcion == "4":
        print(f"Progreso: {calcular_progreso():.1f}%")
    elif opcion == "5":
        break