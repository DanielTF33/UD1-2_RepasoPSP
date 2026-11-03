import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["ping", "8.8.8.8", "-n", "5"], capture_output=True, text=True)

    res_lineas = resultado.stdout.split("\n")

    for linea in res_lineas:
        if "time" in linea or "tiempo" in linea:
            print(linea)