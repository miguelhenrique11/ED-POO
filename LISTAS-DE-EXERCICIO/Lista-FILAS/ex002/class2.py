class Estacionamento:

    #construtor

    def __init__(self):
        self.__dados=[]

    def getEstacionamento(self):
        return(self.__dados)

    def quantidade_carro(self):
        return(len(self.__dados))

    def inserir_Carro(self, novo_carro):
        self.__dados.append(novo_carro)

    def remover_primeiro(self):
        self.__dados.pop(0)

    def remover_Carro(self, carro_informado):
        pos = self.__dados.index(carro_informado)
        i = 0
        while i != pos:
             self.inserir_Carro(self.__dados[i])
             i = i + 1
        for j in range(0, i+1):
             self.remover_primeiro()

