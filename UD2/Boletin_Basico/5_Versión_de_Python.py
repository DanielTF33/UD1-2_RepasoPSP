import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["python", "--version"], capture_output=True, text=True)

    print(resultado.stdout)