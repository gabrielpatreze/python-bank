from conta import Conta
from cliente import Cliente

#print('>> CADASTRO DE CLIENTE que tem: nome, cpf, idade
cliente1 = Cliente('Gabriel John', '111.111.111.10', 26)
#cliente2 = Cliente('Ivonete', '222.222.222.20', 63)

#print('>> CADASTRO DA CONTA que tem: numero da conta, saldo, limite
conta1 = Conta(23309.15, 200, 1000)
#conta2 = Conta('Ivonete Cruz', 100, 1000)
print('')
print('>> CONTA DO CLIENTE <<')
print('Nome do cliente: ', cliente1.nome)
print('CPF:', cliente1.cpf)
print('Idade:', cliente1.idade)
print('Número da conta: ', conta1.numero)
print('Saldo: $', conta1.saldo)
print('Limite: $', conta1.limite)
print('')

conta1.depositar(1000)
print('Número da conta:', conta1.numero)
print('>> por', cliente1.nome)
print('Seu saldo atual é: $', conta1.saldo)
print('')

conta1.saque(200)
print('Número da conta:', conta1.numero)
print('>> por', cliente1.nome)
print('Seu saldo atual é: $', conta1.saldo)
print('')

conta1.saque(2200)
print('Número da conta:', conta1.numero)
print('>> por', cliente1.nome)
print('Seu saldo atual é: $', conta1.saldo)
print('')

conta1.depositar(15000)
print('Número da conta:', conta1.numero)
print('>> por', cliente1.nome)
print('Seu saldo atual é: $', conta1.saldo)
print('')