import subprocess

import time

if __name__ == '__main__':

    notepad = subprocess.Popen(["notepad.exe"])
    paint = subprocess.Popen(["mspaint.exe"])

    print(f"Notepad {notepad.pid} y Paint {paint.pid}")

    time.sleep(5)

    notepad.terminate()
    paint.terminate()
