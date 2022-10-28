# Crie um programa para ler o nome, ano de
# nascimento e sexo de diferentes pessoas
# Armazene os dados em um dicionário com listas
# Ao encerrar o cadastro, apresente:
# O total de cadastros efetuados (falta fazer)
# A média das idades das pessoas (falta fazer)
# Uma lista de mulheres com menos de 30 anos (falta fazer)
# Uma lista de homens com idade acima da média (falta fazer)

#Funções:
def escolhagenero():
    Genero = input('Digite seu Gênero (m/f): ')
    if Genero.lower() == 'm':
        Genero = 'Masculino'
    elif Genero.lower() == 'f':
        Genero = 'Feminino'
    else:
        print('Erro. Escolha M ou F: ')
        escolhagenero()
    print(Genero)
    return Genero

def mediaidade():
    global cadastro
    soma = cadastro['Ano']

def numerocadastro():
    global cadastro
    if cadastro in cadastro:
        print('Número Total de Cadastros: {}.'.format(cadastro['Nome'].count()))



# criação de dicionário. cadastro vazio[]
cadastro = { 'Nome':[], 'Genero':[], 'Ano':[]}

while True:
    terminar = input('Deseja cadatrar uma pessoa? (S - Sim ou N - Não): ')
    if terminar.lower() == 'n':
        break
    if terminar.lower() not in 's': # Se não for digitado 's'
        print('Digite S para SIM ou N para NÃO')
        continue # continua a pergunta. Um "laço"

    # Perguntas:
    Nome = input('Digite um Nome: ')
    Genero = escolhagenero()
    Ano = int(input('Digite um Ano: '))

    # inputando no dicionário:

    cadastro['Nome'].append(Nome) # na variável CADASTRO,como é lista, podemos chamar pelo nome(NOME)
                                    # acrescentar na lista do dicionário (Nome)

    cadastro['Genero'].append(Genero)
    cadastro['Ano'].append(Ano)

print(cadastro)
print('Número Total de Cadastros: {}.'.format(cadastro.count()))