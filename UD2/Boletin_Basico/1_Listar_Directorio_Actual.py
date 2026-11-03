import subprocess
from pydoc import text

if __name__ == '__main__':

    resultado = subprocess.run(["dir"], text=True, capture_output=True, shell=True)

    print(resultado.stdout)