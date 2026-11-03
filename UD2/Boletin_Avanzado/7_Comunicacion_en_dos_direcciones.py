import subprocess
import sys

if __name__ == '__main__':

    proceso = subprocess.Popen(
        ["python", "-c", "print(input().upper())"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    salida, error = proceso.communicate(input="hola mundo")
    print(proceso.pid)
    print(salida)