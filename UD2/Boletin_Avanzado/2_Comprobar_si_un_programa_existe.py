import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["where", "python"], capture_output=True, text=True)

    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print("No encontrado")



