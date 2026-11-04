from functools import reduce

numeros = [2, 3, 4, 5]

producto_total = reduce(lambda a, b: a * b, numeros)

print(producto_total)