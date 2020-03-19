from classpilha import Pilha

def main():
    pilha_s=Pilha()
    pilha_aux=Pilha()
    qtde=int(input('QUANTOS ELEMENTOS DESEJA ADICIONAR NA PILHA S? '))
    for i in range(qtde):
        elmt=input(f'{i+1}* ELEMENTO: ')
        pilha_s.push(elmt)
    print(f'PILHA PRIMÁRIA - {pilha_s.showStack()}')
    pilha_s.ordemDescendente()
    for i in range(qtde):
        pilha_aux.push(pilha_s.pop())
    print(pilha_aux.showStack())
    for i in range(qtde):
        pilha_s.push(pilha_aux.pop())
    print(pilha_s.showStack())


main()