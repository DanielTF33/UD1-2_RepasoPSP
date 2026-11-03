import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["hostname"], text=True, capture_output=True)

    print(resultado.stdout.strip())