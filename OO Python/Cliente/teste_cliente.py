#Importando a classe Cliente.
from cliente import Cliente

#Criando objeto.
cliente = Cliente("vinicius lemes")

#Testando a anotação @property que substitui o get.
print(cliente.nome)

#Testando a anotação @nome_atributo.setter que substitui o setter.
cliente.nome = "victor lemes"

#Testando para ver se o nome do cliente foi alterado.
print(cliente.nome)