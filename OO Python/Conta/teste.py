#Teste com a classe Conta
from conta import Conta

#Criando objetos
conta = Conta(123, "Vinicius", 100.0, 1000)
conta2 = Conta(321, "Victor", 55.0, 1000)

#testando o método tranfere
conta.transfere(10.0, conta2)

#Testando o método extrato do objeto conta
conta.extrato()

#Testando o método extrato do objeto conta2
conta2.extrato()

#Vendo o atributo limite do objeto conta usando o get 
print("Limite: {}".format(conta.limite))

#Vendo o atributo saldo do objeto conta usando o get
print("Saldo: {}".format(conta.saldo))

#Vendo o atributo titular do objeto conta usando o get
print("Titular: {}".format(conta.titular))

#Mudando o valor do atributo limite, usando o set no objeto conta
conta.limite = 10000.0

#Verificando se o limite foi mudado após utilizar o set
print("Limite depois de usar o set: {}".format(conta.limite))