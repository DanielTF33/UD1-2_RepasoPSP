class CuentaBancaria:
    def __init__(self, titular, saldo= 0):
        self.titular = titular
        self.saldo = saldo

    def ingresar (self, ingreso):
        if ingreso < 0:
            print("No te quites saldo hombre")
        else:
            self.saldo = self.saldo + ingreso

    def retirar (self, retiro):
        if retiro < 0:
            print("No te retires negativo hombre")
        else:
            self.saldo = self.saldo - retiro

    def __str__(self):
        return f"Titular: {self.titular} — Saldo: {self.saldo} €"

    def __eq__(self, otro):
        return self.titular == otro.titular and self.saldo == otro.saldo

pepe = CuentaBancaria("Pepe", 33000)
pepe.ingresar(3000)
pepe.retirar(33000)
print(pepe)

pepe2 = CuentaBancaria("Pepe", 3000)
print(pepe == pepe2)