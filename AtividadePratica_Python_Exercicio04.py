import random # importado para randomizar as numerações dos vouchers

# Exercício 4:

def existearquivo(bd): # verifica a existência ou não do arquivo.
    try: # tantativas, apra obter sucesso. caso não tenha, entrará em uma exeção.
        verificar = open(bd,'rt') # abrir arquivo (nome do arquivo). r = leitura + t (aquivo de texto)
        verificar.close()
    except FileNotFoundError: # Nome padrão para erros. abre quando se começa digitar.
        return False # retornar falso, coso não achei a função TRY, aqruivo não exista.
    else:
        return True # retornar verdadeiro, coso o arquivo exista.

def criar(bd, Voucher, Nome, Email, Telefone, Curso, Div): # Dados para os inputs dos cadastros
    try:
        abrir = open(bd, 'at')  # a == abrir arquivo e preservar conteúdo + t == arquivo tipo texto
    except:
        print('Erro ao  abrir o arquivo.')  # Erro genérico, criado por mim.
    else:
        abrir.write('\nVoucher:{}\nNome:{}\nEmail:{}\nTelefone:{}\nCurso:{}\n{}'.format(Voucher, Nome, Email, Telefone, Curso, Div))  # write ==  escrever no arquivo.
        # Similar um print, colocando a ordem e o que escrever

    finally:  # Usado para finalizar a função.
        abrir.close()



def listar(bd): # listar, escrever na tela
    try: # ler linha por linha do arquivo
        listar = open(bd, 'rt') # r = leitura + t = tipo do arquivo de texto (.txt)
    except:
        print('Erro ao Ler o Arquivo.')
    else:
        print(listar.read()) # print para mostrar na tela e o 'nome do arquivo'.read() = mostrar todos os dados.
    finally: # Usado para finalizar a função.
        listar.close()



# Programa

bd = 'inscricao.txt' # nome do arquivo para salvar, em texto o bando de dados dos cadastros| inscrições

if existearquivo(bd): # passando o parâmetro para arquivo como TRUE (verdadeiro), entrará nesta IF.
    print('Arquivo Localizado com Sucesso!')

else:
    print('Arquivo NÃO Localizado!!')
    print('Deseja criar o arquivo?: ') # Função criada por minha conta. Não tem no exercício

    menucriacao = int(input('1 - Sim | 2 - Não: '))

    if menucriacao == 1:
        existearquivo(bd) # o argumento "arquivo", está como variável GLOBAL, enquanto o nomearquivo é uma LOCAL.



while True:
    print('\nPrograma de Inscrições do Curso')
    print('\n')
    print('*' * 12 + 'MENU' + '*' * 12)
    print('1 - Inscrição' + '\n' + '2 - Visualizar Inscrição' + '\n' + '0 - Encerrar')

    opcao = int(input('Escolha uma opção: '))

    if (opcao == 1):
        print('*' * 28)
        #print('Opção Escolhida: {}'.format(opcao))
        cadastro = {'Voucher': [], 'Nome': [], 'Email': [], 'Telefone': [],
                    'Curso': []}  # dicionario e lista em aberto para inputar os dados nas respectivas chaves

        for i in range(1):  # Função apra girar a salicitação a inclusão do s 3 dados
            print('-' * 10 + 'INSCRIÇÃO' + '-' * 10)
            Voucher = random.randint(1, 999)
            Nome = input('Digite seu Nome: ')
            Email = input('Digite seu Email: ')
            Telefone = int(input('Digite o seu Telefone: '))
            Curso = input('Digite o Curso: ')
            Div = ('-'*20)
            cadastro['Voucher'].append(Voucher)
            cadastro['Nome'].append(Nome)  # Adicionando na chave 'Nome' os dados em 'Nome"
            cadastro['Email'].append(Email)  # lógica acima
            cadastro['Telefone'].append(Telefone)  # lógica acima
            cadastro['Curso'].append(Curso)  # lógica acima
            criar(bd, Voucher, Nome, Email, Telefone, Curso, Div)
    elif (opcao == 2):
        print('*' * 28)
        #print('Opção Escolhida: {}'.format(opcao))
        print('-' * 4 + 'Lista de Inscritos' + '-' * 4)
        listar(bd)
    elif (opcao == 0):
        print('*' * 28)
        #print('Opção Escolhida: {}'.format(opcao))
        print('Encerrando programa')
        break
    else:
        print('Erro: Digite uma opção válida!') # caso usuário digite uma opção inválida
