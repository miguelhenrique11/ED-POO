from class1 import Pilha
def line():
    return("==========================================================")



def pulaLinnha(num):
    for i in range(num):
        print()
    return(line())

def manual():
    line()
    return("MANUAL DE COMANDOS"
           "\n=========================================================="
           "\n # - APAGA O ULTIMO DIGITO"
           "\n @ - APAGA TODO O TEXTO"
           "\n !! - ENCERRA O PROGRAMA")


def main():
    print(line())
    print("EDITOR")
    print(pulaLinnha(1))
    print(manual())
    print(pulaLinnha(1))

    pilha=Pilha()
    executando=True
    while(executando):
        dgt=input()
        if(dgt=="#"):
            if(pilha.size()>0):
                pilha.pop()
        elif(dgt=="@"):
            if(pilha.size()>0):
                pilha.popAll()
        elif(dgt=="!!"):
            print(pulaLinnha(4))
            print("FIM DO PROGRAMA")
            print(line())
            print("SEU TEXTO")
            executando=False
        else:
            pilha.push(dgt)
        print(pilha.getPilha())
        print(pulaLinnha(4))
main()