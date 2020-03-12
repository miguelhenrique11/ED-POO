class Fila:
    #constructor
    def __init__(self):
        self.__dados=[]

    def tamFila(self):
        return(len(self.__dados))

    def getFila(self):
        return(self.__dados)

    def add(self, new_value):
        self.__dados.append(new_value)

    def remove(self):
        self.__dados.pop(0)

    def bubble_sort(self):
        end= len(self.__dados)
        while(end>0):
            i=0
            while(i<(end -1)):
                if ord(self.__dados[i][end-1]) < ord(self.__dados[i+1][end-1]):
                    auxiliar=self.dados[i]
                    self.__dados[i]=self.__dados[i+1]
                    self.dados[i+1]=auxiliar
                i+=1
            end-=1


class Banco_de_coracoes:

    # constructor
    def __init__(self):
        self.__totalc = 0

    def addCoracoes(self, new_value):
        return (self.__totalc + new_value)

    def retirarCoracoes(self):
        return (self.__totalc - 1)

    def getTotal_coracoes(self):
        return (self.__totalc)


