class Conta:

    ###########################################################################################
    #Está função é o construtor que vai 
    #instanciar um objeto com os seguintes atributos (numero, titular, saldo, limite, codigo_banco),
    #para deixa os atributos encapsulado no python usamos o "__".
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 
        self.__codigo_banco

    ###########################################################################################
    #A função/método extrato mostra o saldo e o titular de um objeto depois de criado,
    #usando a referência self para pegar os valores dos atributos.
    def extrato(self):
        print("Saldo de {}, Titular é o {}".format(self.__saldo, self.__titular))

    ###########################################################################################
    #O método deposita tem duas referências que é o self e o valor,
    #self vai ser usado para pegar o atributo e o valor para atribuir(somar) dentro deste atributo.
    def deposita(self, valor):
        self.__saldo += valor

    ###########################################################################################
    #O método pode_sacar é privado, ele verifica se o valor que está vindo do método saca é 
    #menor que o valor disponivel na conta, retornando um booleano.
    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_sacar
    
    ###########################################################################################
    #O método sacar tem duas referências que é o self e o valor,
    #self vai ser usado para pegar o atributo e o valor para atribuir(subtrair) dentro deste atributo.
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite!".format(valor))

    ###########################################################################################
    #Método transfere recebe três parametros, self é a referência do objeto,
    #o self vai pegar o método saca e retirar o valor que foi informado no segundo parametros,
    #o destino será outro objeto que vai receber o valor informado no saca e depositar no objeto de destino.
    def transfere(self, valor, destino):
        self.saca(valor) 
        destino.deposita(valor)

    ###########################################################################################
    #Criando Getters e Setters.
    #Todo get vai devolver um valor e o set vai inserir um valor nos atributos(saldo, titular e limite).
    #A anotação "@property" ela substitui o get, quando usar a função basta passar
    #o objeto e o nome da função.
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    ###########################################################################################
    #A anotação "@limite.setter" substitui o set, colocando o nome do atributo que deseja modificar o valor,
    #depois passa o ".setter" finalizando a anotação, assim não precisa chamar o set, passando o valor direto
    #no objeto com o nome do método.
    #EX: conta.nome = "Fulano".
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    ###########################################################################################
    #Este método é estatico(staticmethod) pois o não precisa criar um objeto para ver o código do banco,
    #sendo assim você pode chamar o método sem instanciar um objeto.
    @staticmethod
    def codigo_banco():
        return "001"
    
    ###########################################################################################
    #Uma lista de bancos de chave e valor que este método possui, ele também é estatico, podendo
    #ser chamado sem instanciar um objeto.
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}