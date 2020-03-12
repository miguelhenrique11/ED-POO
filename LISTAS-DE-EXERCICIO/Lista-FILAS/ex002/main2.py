from class2 import Estacionamento

def main():

    fila = Estacionamento()

    fila.inserir_Carro("3030 - B")
    fila.inserir_Carro("4040 - C")
    fila.inserir_Carro("5050 - D")
    executando=True
    while(executando):
        dado = input("INSERIR CARRO (ENTRAR) | SITUAÇÃO DO ESTACIONAMENTO (S) | \nRETIRAR CARRO (RM) | ENCERRAR PROGRAMA (CLOSE)| \n QUAL AÇÃO DESEJA REALIZAR?: ")
        print (dado)
        if(dado=="ENTRAR") or (dado=="entrar"):
            placa=input("INFORME A PLACA DO CARRO: ")
            fila.inserir_Carro(placa)
        elif(dado=="S") or (dado=="s"):
            print(f" CARROS PRESENTES: {fila.quantidade_carro()}")
            print(fila.getEstacionamento())
        elif(dado=="RM") or (dado=="rm"):
            placa=input("INFORME A PLACA DO CARRO: ")
            fila.remover_Carro(placa)
        elif(dado=="CLOSE") or (dado=="close"):
            executando=False


    print("Quantidade de carros no estacionamento: ")
    print(fila.quantidade_carro())


main()