import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["hostname"], capture_output=True, text=True)

    print(resultado.stdout.strip())