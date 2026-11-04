productos = []

while True:
    print("----MENU----")
    print("1...Anadir producto")
    print("2...Ver productos")
    print("3...Eliminar producto")
    print("4...SALIR")
    opcion = int(input("DIME OPCION: "))

    if opcion == 1:
        nombre = input("Dime el producto a anadir: ")
        productos.append(nombre)
        print("Anadido con exito")

    if opcion == 2:
        for producto in productos:
            print(producto)

    if opcion == 3:
        eliminar = input("Dime el producto a eliminar: ")
        productos.remove(eliminar)
        print("Eliminado con exito")

    if opcion == 4:
        break
