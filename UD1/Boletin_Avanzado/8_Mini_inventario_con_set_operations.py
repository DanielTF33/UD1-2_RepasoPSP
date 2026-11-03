tienda_a = {"manzana", "plátano", "naranja", "leche"}
tienda_b = {"plátano", "leche", "pan", "huevos"}

print("\nAMBAS")
ambas = tienda_a.intersection(tienda_b)
print(ambas)

print("\nDIFERENCIA")
diferencia = tienda_a.difference(tienda_b)
print(diferencia)

print("\nUNION")
union = tienda_a.union(tienda_b)
print(union)

print("\nDIFERENCIA SIMETRICA")
sime = tienda_a.symmetric_difference(tienda_b)
print(sime)