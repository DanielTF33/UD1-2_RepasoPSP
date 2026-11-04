numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "aprende python en la fp"
cadena = "hola mundo"

pares = [numero ** 2 for numero in numeros if numero % 2 == 0]
longitud = [len(palabra) for palabra in frase.split()]
mayus = [caracter.upper() for caracter in cadena]

print(pares)
print(longitud)
print(mayus)