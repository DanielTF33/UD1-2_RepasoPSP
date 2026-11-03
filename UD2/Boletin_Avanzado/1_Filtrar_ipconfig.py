import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["ipconfig"], capture_output=True, text=True)

    res_lineas = resultado.stdout.split("\n")

    for linea in res_lineas:
        if "IPv4" in linea:
            print(linea)