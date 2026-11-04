import subprocess

import time

if __name__ == '__main__':

    proceso = subprocess.Popen(["notepad.exe"])

    print(proceso.pid)

    time.sleep(3)

    proceso.terminate()
 