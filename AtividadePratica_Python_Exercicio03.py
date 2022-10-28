# Exercício 03:

# Implementar um jogo que é popular entre as crianças: um hotel onde os hospedes
# tem algumas restrições quanto a localização de seu quarto,s eguindo as seguintes regras:

# O rato não pode ficar ao lado do gato
# O cão não pode ficar ao lado do osso
# O gato não pode ficar ao lado do cão
# O queijo não pode ficar ao lado do rato

# O jogo é composto por 4 fases, onde cada fase (a partir da fase 2)
# só é desbloqueada se a anterior for concluida com êxito
# Em todas as fases,a s células em cinza representam os quartos indisponíveis, portanto não
# podem ser alocados. as letras nas células cprrespondem aos sequintes hóspedes:

# G - Gato
# C - Cão
# R - Rato
# O - Osso
# Q - Queijo

# Ao terminar cada fase o jagador deverá receber uma mensagem informando se teve Êxito
# ou não na sua resposta. SE não teve êxito, o programa se encerra mostrando a mensagem:
# "Você Perdeu!". Se teve êxito a próxima fase é desbloqueada, ao terminar a ultima fase
# com exito uma mensagem de "Você Ganhou!" é mostrada na tela

print('HOTEL DOS ANIMAIS\n')

print('Especificando Posição:')
matriz_1=[1,2,3,4]
matriz_2=[5,6,7,8]
print(matriz_1)
print(matriz_2)


print('\nBem Vindo a fase 1:')
# print('Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:')


personagens = [['G','GATO'], ['C','CÃO'], ['R','RATO'], ['O','OSSO'], ['Q','QUEIJO']]

# Fase 1:

def fase1():
    matriz_fase1 = ('* * _ _')
    print(matriz_fase1.split(' '))
    matriz2_fase1 = ('_ _ * *')
    print(matriz2_fase1.split(' '))
    rato = int(input('Em qual posição quer alocar o RATO? '))
    gato = int(input('Em qual posição quer alocar o GATO? '))
    if(rato != 2 and rato != 3 and gato != 0 and gato != 1 ):
        print('Quarto Não Disponível')

# Principal:

fase1()

