# Acesso aos Dados.

import pandas

# Carregando dados. QUe podem ser de um endereço local ou um html. sempre entre aspas. e .arquivo(csv,xlsx, outros)
# Pegar dados com permissão de acesso ou o mais bruto.
dadosprincipal = pandas.read_csv('https://raw.githubusercontent.com/leonhgomes/Pandas/main/pokemon_data.csv')

def columns():
    print(dadosprincipal.columns)
    # print apenas das colunas do arquivo.

def dados():
    print(dadosprincipal.head)
    # Carrega as informações totais do arquivo.

def dadosprincipaisselecionadosup():
    print(dadosprincipal.head(3))
    # quantidade de linhas iniciais (3) + todas as colunas de cima para baixo.
    # três primeiras
    # Pode-se passar uma quantidade de linhas para abrir do arquivo, caso seja estenso em númeor de linhas e colunas.

def dadosprincipaisselecionadosdown():
    print(dadosprincipal.tail(3))
    # quantidade de linhas Finais (3) + todas as colunas
    # Três ultimas

# Acessando Colunas Individuais:

def colunaselecionada():
    print(dadosprincipal['Nome'])
    # mostra apenas a coluna 'Nome' do arquivo.

def colunasselecionadas():
    print(dadosprincipal[['Nome','Tipo 1']])
    # mostra mais de uma coluna. 'Nome' e 'Tipo1' do arquivo.
    # OBS: Tive que usar um colchete para cada coluna que quis mostrar. Ou seja, Duas.

# Acessando Colunas e linhas específicas:

def selecionandodeterminadascolunaselinhas():
    print('1 -  Coluna: Nome e Tipo 1 + Linhas: 5 a 9'+ ' '+'2 -  Coluna: Nome e Tipo 1 + Linhas: 5 a 249+ Pulando de 2 em 2')
    escolha = int(input('Escolha: '))
    if (escolha == 1):
        print(dadosprincipal[['Nome', 'Tipo 1']][5:10]) # Coluna 'NOME" + 'TIPO 1', da linha 5 a 9
    elif(escolha == 2):
        print(dadosprincipal[['Nome', 'Tipo 1']][5:250:5]) # Coluna 'NOME" + 'TIPO 1', da linha 5 a 249, pulando de 2 em 2

# Acessando linhas específicas:

def mostrarlinhas():
    print(dadosprincipal.iloc[:4])
    # localizar do início até a linha 4.

# Acessando linhas e colunas específicas:

def mostrandolinhadeumacolunaespecifica():
    print(dadosprincipal.iloc[2,1])
    # localizar da Linha: 2, Coluna: 1.

# Busca por Nome, ou outro reconhecimento:

def buscapornome():
    print('1- localiza todas as ocorrencias FOGO, contidas dentro da coluna TIPO 1')
    print('2 - Acessar Linha por Nome ')
    escolha = int(input('Escolha: '))
    if(escolha == 1):
        print(dadosprincipal.loc[dadosprincipal['Tipo 1'] == 'Fogo'])
        # localiza todas as ocorrencias 'FOGO', contidas dentro da coluna 'TIPO 1'

# Acessar Linha por Nome:
    # indice e linha foi nomeado ao meu gosto.
    # iterrows - Gera uma lista de linhas, interação pelas linhas do arquivo
    elif(escolha==2):
        for indice, linha in dadosprincipal.iterrows():
            print(indice, linha['Nome']) # coluna alvo para retorno do s dados.
            if linha['#'] == 150: # uma marcação, coluna contida na planilha, pdoeria ser qualquer outra referencia ao meu gosto.
                break               # usar [] para delimitar paramentros em um arquivo

    # Programação retornará o itens de da coluna NOME até a macação númerica, contida na planilha, de 150. e vai parar.

# Valores Estatisticos Básicos:

def valoresemediasdoarquivo():
    print(dadosprincipal.describe())

# Ordenação de Dados:

def ordenacaodedados():
    dadosprincipalordenado=(dadosprincipal.sort_values('Nome'))
    # Organizado de forma ascendente (a-z)
    # nomedavariavel.sort_values('coluna para organização dentrod o arquivo')

    dadosprincipaldesordenado=(dadosprincipal.sort_values('Nome',ascending=False))
    # Organizado de forma descendente (Z-A)
    # "F" maiúsculo.
    print('Dados:')
    print('1 - Ordenado')
    print('2 - Desordenado')
    escolha = int(input('Escolha a ordem dos Dados: '))
    if(escolha == 1):
        print(dadosprincipalordenado)
    elif(escolha == 2):
        print(dadosprincipaldesordenado)


#### Mudanças nos Dados:

def mudancanosdados():
# Modelo cria uma coluna 'Total" somando todos os dados de cada linha e gerando seu total.
    dadosprincipal['Total'] = dadosprincipal['Ataque'] + dadosprincipal['Atq Esp'] + dadosprincipal['Velocidade']
    print('Dados:')
    print('1 - Soma Dos Atributos em uma coluna Total')
    print('2 - Forma Alternativa de Criar uma Coluna Total ')
    print('3 - Remoção de uma Coluna')
    escolha = int(input('Escolha a ordem dos Dados: '))
    if(escolha == 1):
        # Tentar não ter quebra no print
        print('{} - {} - {} - {}'.format(dadosprincipal['Ataque'], dadosprincipal['Atq Esp'], dadosprincipal['Velocidade'], dadosprincipal['Total']))

    elif (escolha == 3): # remove a coluna nome da planilha principal
        removendocoluna = dadosprincipal.drop(columns=['Nome'])
        print(removendocoluna)
    elif(escolha==2): # Forma Alternativa de Criar uma Coluna Total
        soma2=dadosprincipal['Total']=dadosprincipal.iloc[:,4:10].sum(axis=1)
        # Cria uma linha extra chamada Total para mostrar o resultado.
        # iloc -  Pesquisar os dados por indices e não por descrição como no código antigo.
        # [:, 4:9] - O primeiro, antes da [:] vírgula significa as linhas que podemos declarar para a operaçaõ.
            # [:] siginifica todas as linhas. [10:100] siginifica da linha 10 a 100.
        # [:, 4:9]-> 4:9 - Siginifica as matrizes das colunas: 0 = Nome, 1 = Tipo 1, 2 = Tipo 2, etc..
            # no caso, pegando da coluna 4 = Ataque, até 9 = Velocidade
        # sum - função de soma inclusa no python e pandas.
        # axis = eixo. 1 = colunas (axis = 1) e linhas (axis = 0)
        print(soma2)

# Alterando Nomes de Coluna:

def rename():
    renamecoluna=dadosprincipal.rename({'Lendario':'Raro'}, axis=1)
    # (1)Defensa - Qual alterar | (2) Defesa - Alteração
    # axis=1 -> indica que a alteração é na coluna.
    # inplace ->
    print(renamecoluna)

# Alterando Ordem das Colunas:

def reordenandocolunas():
    print('1 - Modo 1')
    print('2 - Modo 2')
    escolha = int(input('Escolha: '))
    if(escolha==1):
        reordenado = dadosprincipal[['Velocidade', 'Defensa', 'Ataque']]
        # Recria uma nova matriz com uma nova ordem e mostra apenas esses
        print(reordenado)
    elif(escolha==2):
        cols = list(dadosprincipal.columns.values)
        # criando a variável cols, com os valores(dados) das colunas
        dados = dadosprincipal[cols[4:0]+[cols[-1]]+cols[4:12]]
        # concatenando as posições das colunas (criada na variável cols)
        print(dados)

# Salvando alterações no arquivo:

def save():
    salvamento=dadosprincipal.to_csv('salvo.csv')
    # salvo.csv - nomeção do arquivo para salvamento.
    # pode acontecer de criar um indice automaticamente.
    #para criar sem indice, use -> ('salvo.csv', index=False)
    print(salvamento)

# Chamando as Funções:

print(' # '*5 + 'Escolha A Função' + ' # '*5 )
print('1 - Mostra Todas as Colunas do arquivo CSV ')
print('2 - Carrega as informações do Arquivo ')
print('3 - As Três Primeiras linhas do Arquivo CSV ')
print('4 - As Três Últimas linhas do Arquivo CSV ')
print('5 - Mostra apenas a coluna: Nome do arquivo CSV. ')
print('6 - Mostra mais de uma coluna: Nome + Tipo1 do arquivo CSV ')
print('7 - Acessando números de Colunas e Linhas específicas do arquivo CSV ')
print('8 - localizar do início até a linha 4 do arquivo CSV ')
print('9 - localizar e mostrar a Linha: 2, Coluna: 1 do arquivo CSV ')
print('10 - localizar por nomes no arquivo CSV ')
print('11 - Valores Estatisticos no arquivo CSV ')
print('12 - Formas de Organização dos dados no arquivo CSV ')
print('13 - Mostrar adicionando coluna extra com algum resultado, Deletar coluna do resultado mostrado no arquivo CSV ')
print('14 - Renomeando no arquivo CSV ')
print('15 - Reordenação de Coluna no arquivo CSV ')
print('100 - Salvar arquivo | Salvar alterações')
print('0 - Sair')
escolha = int(input('Escolha: '))
if(escolha==1):
    columns()
elif(escolha==2):
    dados()
elif(escolha==3):
    dadosprincipaisselecionadosup()
elif(escolha==4):
    dadosprincipaisselecionadosdown()
elif(escolha==5):
    colunaselecionada()
elif(escolha==6):
    colunasselecionadas()
elif(escolha==7):
    selecionandodeterminadascolunaselinhas()
elif(escolha==8):
    mostrarlinhas()
elif(escolha==9):
    mostrandolinhadeumacolunaespecifica()
elif(escolha==10):
    buscapornome()
elif(escolha==11):
    valoresemediasdoarquivo()
elif(escolha==12):
    ordenacaodedados()
elif(escolha==13):
    mudancanosdados()
elif(escolha==14):
    rename()
elif(escolha==15):
    reordenandocolunas()
elif(escolha=='s'):
    print('Salvando Programa...')
    save()
elif(escolha=='x'):
    print('Fechando Programa...')

