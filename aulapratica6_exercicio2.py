# Crie um jogo de pedra, papel ou tesoura
# Jokenpô ). Você deverá jogar contra o
# computador. Você irá sempre escolher uma
# das opções: 1 pedra, 2 papel, 3 tesoura
# O computador irá sempre sortear um número
# de 1 até 3 para jogar
# Armazene todos os resultados em uma lista e
# no final apresente o vencedor
# Encerre o programa ao digitar zero

# funções:
import random # biblioteca importada

# função que valida as entradas (opções)
def valida_int(escolha, min, max):
    x = int(input(escolha))
    while ((x< min) or (x>max)):
        x=int(input(escolha))
    return x
# função que marca quem venceu
# condicional dentro da condicional
def vencedor(jogador1, jogador2):
    global empate, v1, v2 # engloba a variável global em uma local.
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1 # soma + 1 no empate
        elif jogador2 == 2:
            v2 += 1 # soma + 1 na vitoria do computador
        elif jogador2 == 3:
            v1 += 1 # soma + 1 na vitoria do jogador
    elif jogador1 == 2:
        if jogador2 == 1:
            v1 += 1 # soma + 1 na vitoria do jogador
        elif jogador2 == 2:
            empate += 1 # soma + 1 no empate
        elif jogador2 == 3:
            v2 += 1 # soma + 1 na vitoria do computador
    elif jogador1 == 3:
        if jogador2 == 1:
            v2 += 1  # soma + 1 na vitoria do computador
        elif jogador2 == 2:
            v1 += 1  # soma + 1 na vitoria do jogador
        elif jogador2 == 3:
            empate += 1  # soma + 1 no empate
    resultados = [v1, v2, empate] # desconexa. variável local para receber so resultados das opções
      # indices = [0, 1, 2]
    return resultados #  que irá retornar, que é apenas os resultados

# Função Principal

print('Opções do Jogo:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

# escolha = int(input('Qual a sua opção: '))

resultado = [] # variável resultado = 0
jogadas = [] # variável que salva as jogadas

v1 = 0 # variável para vitória do jogador 1
v2 = 0 # variável para vitória do jogador 2
empate = 0 # variável para empate

while True:
    # jogador 1 = j1, pessoa.
    j1 = valida_int('Qual a sua opção: ', 0, 3) # parâmetros que vai se adequar as opções da função
    if not j1: # igual a j1 == 0. se digitar 0 para o jogo
        break
    # jogador 2, que é o computador
    j2 = random.randint(1,3)
    jogadas.append([j1, j2]) # 'variavel'.append() - adiciona e salva um valor ao final de uma lista
                            # lista a ser inputada pelo append [j1 e j2]
                            # a cada jogada vai salvando nesta lista
    print(jogadas) # mostra as variáveis j1 e j2, facultativo observa-las
    resultados = vencedor(j1, j2)  # resultado - variável global, que chama a função vencedor.
    # print(vencedor(j1, j2))        # chamando j1 e j2, informa o resultado
    print('Placar momentâneo: Jogador - Computador - Empate {}'.format(resultados))

# informa os resulatdos gerais:
print('Vitórias do Jogador: {}'.format(resultados[0])) # pega os valores da lista do resulatdo dentro da função vencedor
print('Vitórias do Computador: {}'.format(resultados[1]))
print('Empates: {}'.format(resultados[2]))