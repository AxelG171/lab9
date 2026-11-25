class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
        else:
            print("Monto inválido")

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self._saldo

    def transferir(self, destino, monto):
        if 0 < monto <= self._saldo:
            self.retirar(monto)
            destino.depositar(monto)

c1 = CuentaBancaria("Pedro", 100)
c2 = CuentaBancaria("María", 50)

c1.depositar(200)
c1.obtener_saldo()

c1.retirar(50)
c1.obtener_saldo()
c1.retirar(500)   

c1.transferir(c2, 100)
c1.obtener_saldo()     
c2.obtener_saldo()     