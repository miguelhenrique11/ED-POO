class Fila:

    def __init__(self):
        self.__dados=[]

    def add(self, new_value):
        self.__dados.append(new_value)

    def rmv(self):
        return(self.__dados.pop(0))

    def getFila(self):
        return(self.__dados)

    def tamPilha(self):
        return(len(self.__dados))
