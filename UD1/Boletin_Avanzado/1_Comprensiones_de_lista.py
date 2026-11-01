numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "aprende python en la fp"
cadena = "hola mundo"

cuadrados_pares = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados_pares)

longitudes = [len(palabra) for palabra in frase.split()]
print(longitudes)

mayusculas = [caracter.upper() for caracter in cadena]
print(mayusculas)