from conta import Conta

#Testando métodos estaticos sem instanciar um objeto.
print("Banco do Brasil: {}".format(Conta.codigo_banco()))
print("Bancos: {}".format(Conta.codigos_bancos()))