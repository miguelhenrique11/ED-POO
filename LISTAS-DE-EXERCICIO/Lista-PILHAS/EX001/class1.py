class Pilha:
    def __init__(self):
        self.__dados=[]

    def push(self, new_value):
        self.__dados.append(new_value)

    def pop(self):
        self.__dados.pop()

    def popAll(self):
        while(len(self.__dados)!=0):
            self.__dados.pop()

    def getPilha(self):
        return(self.__dados)

    def size(self):
        return(len(self.__dados))

    def top(self):
        return(self.__dados[len(self.__dados)-1])
