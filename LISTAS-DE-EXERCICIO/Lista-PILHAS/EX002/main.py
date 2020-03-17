from classfila import Fila
from classpilha import Pilha

def main():
    pilha_s = Pilha()
    pilha_aux = Pilha()
    fila_aux = Fila()
    qtde=int(input('Quantos elementos deseja inserir em sua pilha S? '))
    for i in range(qtde):
        element=input(f'{i+1}* Elemento: ')
        pilha_s.push(element)

    print('EX002 - A')
    print(pilha_s.showStack())

    for i in range(qtde):
        pilha_aux.push(pilha_s.pop())
        print(pilha_s.showStack())
    print(pilha_aux.showStack())

main()