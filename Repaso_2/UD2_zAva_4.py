import subprocess

import time

if __name__ == '__main__':

    procesos = ["notepad.exe", "mspaint.exe"]

    diccionario = {}

    for proceso in procesos:
        diccionario[proceso] = subprocess.Popen([proceso])

    for proceso in diccionario:

        print(diccionario[proceso].pid)

    time.sleep(5)

    for proceso in diccionario:
        diccionario[proceso].terminate()
