# Aula prática 02
# Premissa: Manipulação de Dados


import pandas as pd

# registro cliente 01:

cliente_01 = {"nome":"Rafael Gouveia",
              "idade": 38,
              "nacionalidade": "brasileiro",
              "altura":"1.74",
              "peso":80,
              "gênero": "masculino",
              "gosta de futebol":True,
              "salario": 0}

# registro cliente 02:

cliente_02 = {"nome":"Barney Bucho Branco",
              "idade": 6,
              "nacionalidade": "brasileiro",
              "altura":"0.40",
              "peso":12,
              "gênero": "masculino",
              "gosta de futebol":False,
              "salario": 0}

# registro cliente 03:

cliente_03 = {"nome":"Giovana Tavares",
              "idade": 19,
              "nacionalidade": "brasileira",
              "altura":"1.70",
              "peso":60,
              "gênero": "feminina",
              "gosta de futebol":True,
              "salario": 0}

# registro cliente 04:

cliente_04 = {"nome":"Pollyanna Maia",
              "idade": 26,
              "nacionalidade": "brasileira",
              "altura":"1.70",
              "peso":60,
              "gênero": "feminina",
              "gosta de futebol":False,
              "salario": 0}


# OBS: O modelo sempre espera números.

todos_os_clientes = [[38,0,1.74,80,0,1,0],
                     [6,0,0.40,12,0,0,0],
                     [19,0,1.70,60,1,1,0],
                     [26,0,1.70,60,1,0,0],
                     [22,0,1.70,75,0,1,2500],
                     [52,1,1.75,80,0,1,2500],
                     [31,1,1.50,65,1,1,4500],
                     [17,0,1.81,95,0,1,1500],
                     [54,0,1.65,80,1,0,3500],
                     [30,0,1.90,105,1,1,1200],
                     [25,1,1.85,65,1,1,2245],
                     [49,0,1.71,75,0,0,25000],
                     [26,1,1.81,80,1,1,8000]]

df_clientes = pd.DataFrame(data=todos_os_clientes,columns=["Idade",
                                                           "Nacionalidade",
                                                           "Altura",
                                                           "Peso",
                                                           "Genero",
                                                           "Gosta de Futebol?",
                                                           "Salario"])

# Exibe os dados do dataframe em formato tabular
# Convertendo os dados do DF para string
print("\nDados do dataframe organizados de forma tabular\n")
print(df_clientes.to_string())

# Exibe os dados do dataframe como CSV. apenas mostra na tela um arquivo em formato .CSV
# sep "," - Indica que a separação dos dados será por vírgula.
# index (false) - Indica que não terá um index, não armazenará uma coluna de index no arquivo .CSV
# Cada vez que rodar, ele atualizará os dados existntes. Ou seja, apagrá o antigo e gravará por cima.
print("\nDados do dataframe organizados como CSV\n")
print(df_clientes.to_csv(sep=",", index=False))

# Armazena os dados do dataframe em um arquivo CSV. Salvando um arquivo para .CSV
# "dados_clentes.csv" - Nome do arquivo .csv
# index (false) - Indica que não terá um index, não armazenará uma coluna de index no arquivo .CSV

df_clientes.to_csv("dados_clentes.csv", index=False)


# Armazena dos dadosdo dataframe em um arquivo JSON.
# Lembrando um dicionário
# "Dados_clientes.json - o nome do arquivo .CSV para ser criado.
# orient = "records" - Terá o texto da coluna.
# sem o orient - Terá números, e nãos os textos, indicando a separação e orientação por colunas.
# Cada vez que rodar, ele atualizará os dados existntes. Ou seja, apagrá o antigo e gravará por cima.
df_clientes.to_json("Dados_Clientes.json", orient="records")
df_clientes.to_json("dados_clientes_norient.json")

# OBS: os arquivos do tipo CSV, vamos precisar da biblioteca CSV
import csv

# Carrega os dados dos clinetes armazenados no arquivo csv
# delimiter = ',' - separador dos dados.
# quotechar='"' - delimitador de inicio e final de cada coluna. poderia ser chaves, aspas, colchetes.
# f - apelido que batizamos a abertura do arquivo .csv
with open("dados_clentes.csv") as f:
    data = csv.reader(f, delimiter = ',', quotechar='"')
    # Itera as linhas do arquivo
    for linha in data:
        print(str(linha))

print("\n")
print("-"*60)
print("\n")

# Carrega os dados dos clinetes armazenados no arquivo json

import json

# Exemplo orientado aos dados dos registros
dados_clientes_json = None
with open("Dados_Clientes.json", "r") as read_file:
    # Itera as linhas do arquivo
    dados_clientes_json = json.load(read_file)

print(dados_clientes_json)

print("\n")
print("-"*60)
print("\n")

# Exemplo NÂO orientado aos dados dos registros
# Note como os campos são representados

dados_clientes_json_no = None
with open("dados_clientes_norient.json", "r") as read_file:
    # Itera as linhas do arquivo
    dados_clientes_json_no = json.load(read_file)

print(dados_clientes_json_no)

print("\n")
print("-"*60)
print("\n")

# Executando o dump string de uma lista com dois dicionários para json
# Convertendo os dois dicionário na variavel cliente_xx para json
# para converter, usamso a chamada json.dumps - convertendo o q tem de json para uma string,
# mas simula, mas nãoé um dicionário
# No fim das contas, tudo isso no json é texto

print("Tipo da variável cliente_01: ", type(cliente_01))
print("Tipo da variável cliente_02: ", type(cliente_02))
print("Tipo da variável cliente_03: ", type(cliente_03))
print("Tipo da variável cliente_04: ", type(cliente_04))

print(str(json.dumps([cliente_01,cliente_02,cliente_03,cliente_04])))

print("\n")
print("-"*60)
print("\n")

# Convertendo o dataframe pandas para XML
# Pegamos as informações da variável clientes_xx - df_2clientes = pd.DataFrame([cliente_01,cliente_02,cliente_03,cliente_04])
# xml é orinetado a resgistros, orientado à dados.
# as separações entre so reguistros são bem visiveis, bem claras.
# simliar a abertura e fechamndo de html

def to_xml(df, filename=None, mode='w'):
    def row_to_xml(row):
        xml= ['cliente']
        for i, coluna_nome in enumerate (row.index):
            xml.append('<atributo name ="{0}">{1}</atributo>'.format(coluna_nome, row.iloc[i]))
        xml.append('<cliente>')
        return '\n'.join(xml)
    res = '\n'.join(df.apply(row_to_xml, axis=1))

    if filename in None:
        return res
    with open (filename, mode) as f:
        f.write(res)

pd.DataFrame.to_xml = to_xml

df_2clientes = pd.DataFrame([cliente_01,cliente_02,cliente_03,cliente_04])
# df_2clientes.to_csv() # convertendo para CSV
str_xml=df_2clientes.to_xml()
print(str(str_xml))