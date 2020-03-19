from classpilha import Pilha

def main():
    pilha_s1=Pilha()
    pilha_s2=Pilha()
    pilha_aux=Pilha()
    print('EX004 - A\n')
    qtde=int(input('QUANTOS ELEMENTOS DESEJA INSERIR NA PILHA S1? '))
    for i in range(qtde):
        pilha_s1.push(input(f'{i+1}* ELEMENTO: '))
    for i in range(qtde):
        pilha_aux.push(pilha_s1.pop())
    for i in range(qtde):
        elm=pilha_aux.pop()
        pilha_s1.push(elm)
        pilha_s2.push(elm)
    print(f'PILHA S1 - {pilha_s1.showStack()}')
    print(f'PILHA S2 - {pilha_s2.showStack()}\n')
    print('EX004 - B\n')
    pilha_s1.popAll()
    pilha_s2.popAll()
    qtde=int(input('QUANTOS ELEMENTOS IRÁ ADICIONAR NA PILHA S1? '))
    str=''
    for i in range(qtde):
        elm=(input(f'{i+1}* ELEMENTO: '))
        str+=elm
        pilha_s1.push(elm)
        str+=' '
    print(f'PILHA S1 - {pilha_s1.showStack()}')
    plv=''
    for i in range(len(str)):
        l=str[i]
        if(l!=' '):
            plv+=l
        else:
            pilha_s2.push(plv)
            plv=''
    print(f'PILHA S2 - {pilha_s2.showStack()}')
main()