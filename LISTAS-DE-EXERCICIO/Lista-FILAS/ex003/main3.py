from class3 import Fila
from class3 import Banco_de_coracoes

def linha():
    return("="*50)

def receberCoracoes(qtde_coracoes, value):
        return(qtde_coracoes+value)
def main():
    fila = Fila()
    coracoes= Banco_de_coracoes
    executando=True
    while(executando):
        print("BEM VINDO AO MENU PRINCIPAL")
        print(linha())
        option=input("CADASTRO (1) \nTAMANHO DA FILA (2) \nBANCO DE CORAÇÕES(3) \nENCERRAR PROGRAMA(4) \nQUAL AÇÃO DESEJA REALIZAR? ")
        if(option=='1'):
            print("INFORME: \nNOME -  TELEFONE - GRAU DE URGENCIA ")
            fila.add()

main()