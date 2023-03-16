#Importando classe conta
from conta import Conta

#Criando onjeto conta
conta = Conta(123, "Vinicius", 100.0, 1000)

#Verificando se pode sacar, nesse teste vai exibir que ultrapassou o limite da conta,
#pois o valor a sacar é maior que o limite.
conta.saca(2000.0)

#Verificando se o saque foi bem sucedido e se mudou o saldo.
conta.saca(200.0)
print(conta.saldo)