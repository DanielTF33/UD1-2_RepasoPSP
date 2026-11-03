import subprocess


def reintentos(comando):

    for i in range(1,4):
        try:
            resultado = subprocess.run(comando, timeout=3, check=False, capture_output=True, text=True)

            if resultado.returncode == 0:
                print(f"Perfecto ha salido bien {resultado.stdout.strip()}")
                return resultado

            print(f"Intento numero {i} nada eh")

        except subprocess.TimeoutExpired:
            print(f"BAAAA error tiempo agotado, intento {i}")
        raise TimeoutError("EXPLOSION ameisin")


if __name__ == '__main__':

    try:
        resultado = reintentos(["ping", "8.8.8.8", "-n", "3"])
    except TimeoutError as e:
        print(e)