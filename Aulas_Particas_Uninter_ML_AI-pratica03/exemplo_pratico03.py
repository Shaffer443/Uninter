# Aula Prática 03 - Aprendizagem Supervisionada - Parte I
# Preparação dos Dados:
# Obter a base de dadis cin a qual irá trabalhar deve passar por, pelo menos, 3 etapas:
# 1 -  Formatação/Padronização
# 2 - Ajustes/Correção dos Dados
# 3 - Seleção dos Dados

import pandas as pd

carros = pd.read_csv("carros.csv")
print(carros)
print("\n"*3)

# info tamanho dataset:
print(carros.shape)
print("\n"*3)

# Info - NOme das colunas:

print(carros.columns)
print("\n"*3)

# Preenchedno dados faltantes, por qualquer motivo que seja
# tratando os dados - parte 1
# preencher os dados faltantes
# .fillna - Permite colcoar valores, onde não há valores. Onde não há valor definido

carros['categoria'].fillna('INDEFINIDO', inplace=True)
carros['combustivel'].fillna('Alcool', inplace=True)
carros['num_portas'].fillna(2., inplace=True)

# Convertendo as colunas para categorias
# .astype - Informa que transforme tal coluna em na categoria determinada
# associado a numeros.
# exemplo: alcool - 1, gasolina - 2, gnv -3  e etc
# todas as colunas solicitadas,s erá transformada em números

carros['combustivel']= carros['combustivel'].astype('category')
carros['tipo_transmissao']= carros['tipo_transmissao'].astype('category')
carros['categoria']= carros['categoria'].astype('category')
carros['tamanho']= carros['tamanho'].astype('category')
carros['estilo']= carros['estilo'].astype('category')
carros['label']= carros['label'].astype('category')

# Substitui os valores das colunas categoricas (categoty) pelos valores numericos

cat_columns = carros.select_dtypes(['category']).columns
carros[cat_columns] = carros[cat_columns].apply(lambda x: x.cat.codes)
print(carros)
print("\n"*3)

# Fatiando o DataFrame
# pegando de uma determina coluna, passada pelos eu nome, até o final(no caso)
# cortando algumas colunas que não interessa no momento, no caso fabrincante e modelo
# pegadno todas as linhas à partir da coluna 'ano'

print(carros.loc[:, 'ano':])
print("\n"*3)

# Salvando o arquivo após edição, para evitar ficar sempre fazendo
# opererações de cortes na planilha

try:
    carros.to_csv("carros_edit01_categororias.csv", index=False)
    print("Arquivo Criado com sucesso !")
    print("\n" * 3)
except:
    print("Erro. Falha ao criar ou salvar o arquivo.")