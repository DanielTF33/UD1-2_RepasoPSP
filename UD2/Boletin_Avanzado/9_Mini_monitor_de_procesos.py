import subprocess
import time

if __name__ == '__main__':

    proceso = subprocess.Popen(["mspaint.exe"])

    while proceso.poll() is None:
        print("Sigue vivo el paint jaja")
        time.sleep(1)

    print("Acabas de cerrarlo")