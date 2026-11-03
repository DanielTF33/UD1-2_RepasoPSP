import subprocess

import time

if __name__ == '__main__':

    proceso = subprocess.Popen(["calc.exe"])

    print(f"ID del proceso {proceso.pid}")

    time.sleep(2)
    proceso.terminate()