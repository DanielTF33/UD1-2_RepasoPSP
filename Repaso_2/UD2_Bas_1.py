import subprocess

if __name__ == '__main__':

    resultado = subprocess.run(["dir"], capture_output=True, text=True, shell=True)

    print(resultado.stdout)