# Suponha que você é um colecionador de jogos de videogame. Escreve um algoritimo
# que permita cadastrar esses jogos informando o nome e a qual videogame ele pertence.
# Para isso, crie um meni de opç~eos contendo: Cadastrar novo item, listar tudo que foi cadastrado e sair.
# Para resolver esse execício, crie pelo menos uma função para cada item do menu.
# Armazene todos os dados em uma arquivo de texto que deve ser salvo em disco e mantes
# os dados cadastrados.

# Funções - Ferramenta para o programa principal:

# OBS: Na função principal arquivo. Nas funções, chama-se nomearquivo.
# São a mesma coisa para locais destintos e tarafas pontuais.

#Função para vailidar as opções diposniveis no MENU principal:

def validacaointeiro(pergunta, min, max): # pode ser criada antes ou depois da função fatorial
    x = int(input(pergunta))              # forçar o usuário a inserir núemro interio e não muito alto. essa é a premissa.
    while((x < min) or ( x > max)): # validar o intervalo dentro do parâmetros que queremos.
        x = int(input(pergunta))
    return x # valor para vaidação e também servira para o input a ser fatorado


#Função para CRIAR um arquivo .txt:
def criaarquivo(nomearquivo): # função para criar o arquivo.
    try: # tentativa para criar o arquivo.
        criar = open(nomearquivo, 'wt+') # + == Caso o arquivo não exista, ele cria. w == abrir arquivo para escrita + t = tipo texto
        criar.close()
    except: # Como Criei um tipo de erro gnérico, não precisei "declarar" um erro especifico.
        print("Erro na Criação do Arquivo") # Erro genérico, criado por mim.
    else:
        print('Aquivo {} criado com SUCESSO !!'. format(nomearquivo))


# Função para VERIFICAR existência de um arquivo .txt:
def existearquivo(nomearquivo): # verifica a existência ou não do arquivo.
    try: # tantaivas, apra obter sucesso. caso não tenha, entrará em uma exeção.
        verificar = open(nomearquivo,'rt') # abrir arquivo (nome do arquivo). r = leitura + t (aquivo de texto)
        verificar.close()
    except FileNotFoundError: # Nome padrão para erros. abre quando se começa digitar.
        return False # retornar falso, coso não achei a função TRY, aqruivo não exista.
    else:
        return True # retornar verdadeiro, coso o arquivo exista.

#Função Cadastrar Jogo:

def cadastrar(nomearquivo, nomejogo, nomeconsole ): # Gera o arquivo + nome do jogo digitado + nome do console
    try:
        abrir = open(nomearquivo, 'at') # a == abrir arquivo e preservar conteúdo + t == arquivo tipo texto
    except:
        print('Erro ao  abrir o arquivo.') # Erro genérico, criado por mim.
    else:
        abrir.write('{} - {} \n'.format(nomejogo, nomeconsole)) # write ==  escrever no arquivo.
                                                                 # Similar um print, colocando a ordem e o que escrever
        # melhorias: Criar contador para o numero de jogos e viasualização mellhor do print de forma automata
    finally: # Usado para finalizar o programa.
        abrir.close()

# Função LISTAR arquivo:

def listar(nomearquivo): # listar, escrever na tela
    try: # ler linha por linha do arquivo
        listar = open(nomearquivo, 'rt') # r = leitura + t = tipo do arquivo de texto (.txt)
    except:
        print('Erro ao Ler o Arquivo.')
    else:
        print(listar.read()) # print para mostrar na tela e o 'nome do arquivo'.read() = mostrar todos os dados.
    finally: # Usado para finalizar o programa.
        listar.close()

### Programa Principal ###

arquivo = 'cadastrogames.txt' # aspas simples, pois o nome do arquivo é um string


if existearquivo(arquivo): # passando o parâmetro para arquivo como TRUE (verdadeiro), entrará nesta IF.
    print('Arquivo Localizado com Sucesso!')
else:
    print('Arquivo NÃO Localizado!!')
    print('Deseja criar o arquivo?: ') # Função criada por minha conta. Não tem no exercício

    menucriacao = int(input('1 - Sim | 2 - Não: '))

    if menucriacao == 1:
        criaarquivo(arquivo) # o argumento "arquivo", está como variável GLOBAL, enquanto o nomearquivo é uma LOCAL.
    else:
        validacaointeiro('Escolha a opção do MENU: ', 1, 3) # Pergunta+parâmetros(min e max == 1, 3)




while True: # usado por não saber o número de cadastros de iténs que será feito e salvo.
    print('MENU')
    print('1 - Cadastrar Item')
    print('2 - Listar Cadastro')
    print('3 - Sair')

    menu = validacaointeiro('Escolha a opção no MENU: ', 1, 3) # Pergunta+parâmetros(min e max == 1, 3)

    if menu == 1:
        print('Cadastrar Novo Item\n')
        nomejogo = input('Nome do Jogo: ')
        nomeconsole= input('Nome do Console(VideoGame): ')
        cadastrar(arquivo, nomejogo, nomeconsole) # OBS: nomearquivo (na função é local) == arquivo (global)
    elif menu == 2:
        print('Lista de Cadastro\n')
        listar(arquivo)
    elif menu == 3:
        print('Saindo do Programa de Cadastro.')
        print('Fechando...')
        break