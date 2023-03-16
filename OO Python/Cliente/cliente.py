#Criando a classe Cliente
class Cliente:
    #Gerando o construtor
    def __init__(self, nome):
        self.__nome = nome

    #A anotação "@property" ela substitui o get, quando usar a função basta passar
    #o objeto e o nome da função.
    #O método title coloca a primeira letra de qualquer string como maiuscula e o restande minuscula.
    @property
    def nome(self):
        return self.__nome.title()
    
    #A anotação "@nome.setter" substitui o set, colocando o nome do atributo que deseja modificar o valor,
    #depois passa o ".setter" finalizando a anotação, assim não precisa chamar o set, passando o valor direto
    #no objeto com o nome do método.
    #EX: cliente.nome = "Fulano".
    @nome.setter
    def nome(self, nome):
        self.__nome = nome