from classfila import Fila
from classpilha import Pilha

def main():
    pilha_s=Pilha()
    pilha_aux=Pilha()
    pilha_aux_2=Pilha()
    fila_aux=Fila()
    qtde=int(input('Quantos elementos deseja inserir em sua pilha S? '))
    for i in range(qtde):
        element=input(f'{i+1}* Elemento: ')
        pilha_s.push(element)

    print('EX002 - A\n')
    print(f'PILHA S INICIAL - {pilha_s.showStack()}')
    for i in range(qtde):
        pilha_aux.push(pilha_s.pop())
    print(f'PRIMRIRA PILHA AUXILIAR - {pilha_aux.showStack()}')
    for i in range(qtde):
        pilha_aux_2.push(pilha_aux.pop())
    print(f'SENGUNDA PILHA AUXÍLIAR - {pilha_aux_2.showStack()}')
    for i in range(qtde):
        pilha_s.push(pilha_aux_2.pop())
    print(f'PILHA S FINAL <INVERTIDA> - {pilha_s.showStack()}\n')
    print('EX002 - B\n')
    opt=input('DESEJA MANTER OU ALTERAR SUA PILHA S FINAL? (M / A)').lower()
    if(opt=='a'):
        pilha_s.popAll()
        qtde=int(input('QUANTOS ELEMENTOS DESEJA ADICIONAR EM SUA NOVA PILHA? '))
        for i in range(qtde):
            pilha_s.push(input(f'{i+1}* ELEMENTO: '))
        print(f'NOVA PILHA S - {pilha_s.showStack()}')
        for i in range(qtde):
            fila_aux.add(pilha_s.pop())
    else:
        print(f'PILHA S ATUAL - {pilha_s.showStack()}')
        for i in range(qtde):
            fila_aux.add(pilha_s.pop())
    print(f'FILA AUXILIAR - {fila_aux.getFila()}')
    for i in range(qtde):
        pilha_s.push(fila_aux.rmv())
    print(f'PILHA S FINAL <INVERTIDA> {pilha_s.showStack()}')



main()