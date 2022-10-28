# Dicionários:

# Estrutra de dados dinâmica
# Podemos alterar dados e tamanho
# Indexados por palavras-chaves. Não necessariamente precisa ser números como na lista, tuplas ou matrizes
# Representados em python por chaves {}

#    Chave(index)      Dado
game = {'nome' : 'Super Mário', 'Desenvolvedora' : 'Nintendo', 'Ano' : 1990}
print(game)

# Chamando dado através da chave:
print('\n')
#           Chave
print(game['nome'])
print(game['Desenvolvedora'])
print(game['Ano'])

# Método para Dicionários:

# values: Obtém somente os dados.
# keys: Obtém somente as chaves.
# items: Obtém o par chave:dado.

print(game.values()) # retorna todos os dados da inclusos na variável game

# imprimindo os dados pelo FOR:
print('\n')
for i in game.values(): # varre os dados da variável game
    print(i)

# informando as chaves:
print('\n')
print(game.keys())

# através da varredura
print('\n')
for i in game.keys():
    print(i)

# informando as chaves e dados:
print('\n')
print(game.items())

# através da varredura
print('\n')
for i in game.items():
    print(i)

# Lista com Dicionarios:
print('\n')

jogos = [] # lista que receberar os dados declarados

game1 = {'nome': 'Resident Evil', 'Console': 'Playstation', 'Ano': 1996}
game2 = {'nome': 'God Of War 3', 'Console': 'Playstation 3', 'Ano': 2008}
game3 = {'nome': 'Uncherted', 'Console': 'Playstation 3', 'Ano': 2012}

games = [game1, game2, game3] # incluindo todos os dados na variável GAMES
print(games) # retorna os uma LISTA dados da variável GAMES

# incluindo dados através do usuário:
print('\n')

jogo = {} # variável que recebera todos dados inputados
dvd_jogos = [] # alocará os dados recebidos em uma nova variável

for i in range(3):
    jogo['Nome'] = input ('Nome do jogo: ') # Informo o nome da chave e em seguido pergunto o dado ser inserido.
    jogo['Console'] = input('Plataforma do jogo: ')  # Informo o nome da chave e em seguido pergunto o dado ser inserido.
    jogo['Status'] = input('Situação no jogo: ')  # Informo o nome da chave e em seguido pergunto o dado ser inserido.
    dvd_jogos.append(jogo.copy()) # Copiando os dados em uma nova alocaçãod e memória
print('-'*20)
for e in dvd_jogos: # modo de varres os dados na lista
    for s,b in e.items(): # e == variável de busca nomeada para o primeiro FOR. ITEMS variável q varre chaves e dados. Busca nos dicionários
        print('{} - {}'.format(s,b)) # listando so dados de duas informações

# Dicionário com listas:
print('\n')

gamesplaystation = {'Nome':['Uncherted', 'God Of War', 'Battlefiel 4'], 'Console':['PS3', 'PS4', 'PS5'], 'Status':['Zerado', 'Jogando', 'Não Iniciado']}
print(gamesplaystation)

# Inserir dados pelo usuário:

jogosps ={'Nome':[], 'Console':[], 'Status':[]} # dicionario e lista em aberto para inputar os dados nas respectivas chaves

for i in range(3): # Função apra girar a salicitação a inclusão do s 3 dados
    Nome = input('Digite o nome do Jogo: ')
    Console = input('Digite o console do Jogo: ')
    Status = input('Digite o andamento do Jogo: ')
    jogosps['Nome'].append(Nome) # Adicionando na chave 'Nome' os dados em 'Nome"
    jogosps['Console'].append(Console) # lógica acima
    jogosps['Status'].append(Status) # lógica acima
print(jogosps)