# 7. Comunicación en dos direcciones
#
# Crea un proceso hijo que reciba texto por stdin y devuelva el texto en mayúsculas.
#
#Pista: usa subprocess.Popen con stdin=subprocess.PIPE, stdout=subprocess.PIPE y
#text=True. Luego llama a communicate(input="tu texto") para enviar datos y leer la
#respuesta.
#
import subprocess

if __name__ == '__main__':

    resultado = subprocess.Popen(["python", "-c", "print(input().upper())"], text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


    salida, error = resultado.communicate("si si si si si si si no")

    print(salida)

    if "NO" in salida:
        print("COMO QUE NO")