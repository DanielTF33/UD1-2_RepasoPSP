import subprocess

import time

apps = ["notepad.exe", "mspaint.exe"]

lista_procesos = []

for app in apps:
    lista_procesos.append((app, subprocess.Popen([app])))

print(lista_procesos)

time.sleep(5)

diccionario_procesos = {}

for app in apps:
    diccionario_procesos[app] = subprocess.Popen([app])

print(diccionario_procesos)

for valor in diccionario_procesos.values():
    print(valor)

for key in diccionario_procesos.keys():
    print(key)

for clave, valor in diccionario_procesos.items():
    print(clave, valor)