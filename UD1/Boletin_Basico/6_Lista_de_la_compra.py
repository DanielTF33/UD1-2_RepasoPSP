compra = []

while True:

    print("----MENU----")
    print("1...Añadir un producto a una lista")
    print("2...Ver todos los productos")
    print("3...Eliminar un producto")
    print("4...SALIR")
    opcion = int(input("Di una opcion"))

    if opcion == 1:
        nombre = input("Dime el producto")
        compra.append(nombre)
    elif opcion == 2:
        print(compra)
    elif opcion == 3:
        eliminar = input("Producto a eliminar")
        compra.remove(eliminar)
    elif opcion == 4:
        print("ADIOOOOOOS")
        break
