import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["ipconfig"], capture_output=True, text=True)

    lineas = resultado.stdout.split("\n")

    for linea in lineas:
        if "IPv4" in linea:
            print(linea)