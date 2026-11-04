import subprocess

if __name__ == '__main__':

    try:
        resultado = subprocess.run(["ping", "8.8.8.8", "-n", "3"], capture_output=True, text=True, timeout=3)

        print(resultado.stdout)
    except subprocess.TimeoutExpired:
        print("Se ha agotado el tiempo")





