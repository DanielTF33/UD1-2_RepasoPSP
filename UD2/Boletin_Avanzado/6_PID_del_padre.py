import os

if __name__ == '__main__':

    print(f"Hijo = {os.getpid()}")
    print(f"Padre = {os.getppid()}")