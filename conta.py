class Conta():
    def __init__(self, numero, saldo, limite):
        self.numero = numero
        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, dinheiro):
        if dinheiro > 0:
            self.saldo += dinheiro
            print('>> DEPÓSITO <<')
            print('Foi depositado $', dinheiro)
        else:
            print('Tente novamente!')

    def consulta_saldo(self):
        return self.saldo


    def saque(self, dinheiro):
        if  self.saldo - dinheiro < self.limite:
            print('>> Saque inválido! <<')
            print('Você tentou sacar $', dinheiro)
            print('Mas seu limite é $', self.limite, ', tente outro valor!')
        else:
            self.saldo -= dinheiro
            print('>> SAQUE <<')
            print('Você sacou $', dinheiro)


