import subprocess

proceso = subprocess.Popen(
    ["python", "-c", "print(input().upper())"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)


salida, _ = proceso.communicate(input="hola mundo")
print(f"El proceso respondió: {salida.strip()}")
# → "HOLA MUNDO"


import subprocess

proceso = subprocess.Popen(
    ["ipconfig"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

salida, errores = proceso.communicate()

print(salida)