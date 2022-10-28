# Aula Prática 03 - Aprendizagem Supervisionada - Parte II
# Preparação dos Dados, Separação dos Dados e TReinamento de um DT:
# Obter a base de dados na qual irá trabalhar deve passar por, pelo menos, 3 etapas:
# 1 -  Formatação/Padronização
# 2 - Ajustes/Correção dos Dados
# 3 - Seleção dos Dados

import pandas as pd
from sklearn import tree
import graphviz
import numpy as np


# Exemplo didatico de uma árvore:
# Algoritimo de classificação supervisionada

df_clientes = pd.read_csv(r"dados_clientes_nome.csv")
print(df_clientes)
print("\n"*3)

# Preparando um conjunto de dados para um algoritimo de árvore de decisão.
# Treina um algoritmo de árvore de decisão com os dados

# indicando nome das colunas
atributos = ['idade', 'nacionalidade', 'altura', 'peso', 'sexo', 'salario']

# processo de seleção, fatiamento do DataFrame
# porém pegando apenas todas as colunas passada na variável 'atributos'
# colocando dentro de um Data Frame 'df_clientes' e convertendo para numpy
x_treino = df_clientes.loc[:, atributos].to_numpy()

# Carregando a nossa variável indepednete
# vetor de caracteristicas(referência para comparação) de todos os clientes
# buscando a informação se p cliente gosta de futebol ou não
# y_treino = label (referência independente)
y_treino = df_clientes['gosta de futebol'].to_numpy()

# Algoritnom de classificação
# classificador de árvore de decisão
# precisamos passar os criterios de divisão
# criterion = 'gini' - qual o indice que ele usa para fazer o processo de divisão na árvore
# splitter = 'best' - processo de divisão, com ele separa os ramos, as folhas da árvore
# max-depth - profundidade máxima que essa árvore vai atingir | 10 é pq temos 10 linhas no modelo
# min_samples_split - númeor mínimo de amostra para que se faça uma divisão
# max_features - máximo de atributos utilizados

clf=tree.DecisionTreeClassifier(criterion= "gini", splitter="best",
                                max_depth=10, min_samples_split=5,
                                min_samples_leaf=1, max_features=6)

# Processo de treinamento do modelo
# modelo de aprendizagem em sí
# .fit - processo de aprendizagem, de treinamento
clf = clf.fit(x_treino, y_treino)

# uso do graphviz

categorias_gosta_futebol = ['não gosta futebol', 'gosta futebol']
dot_data = tree.export_graphviz(clf, out_file=None, filled=True,
                                rounded=True,
                                special_characters=True,
                                feature_names=atributos,
                                class_names=categorias_gosta_futebol)

graph = graphviz.Source(dot_data)
#graph.render("futebol_tree") # salvando os dados em um arquivo
                            # debugou sem o .render
print(graph)
print("\n"*3)
# -----------------------------------------------------------------------------------------------
# Modelo 02

# Usando dados de treino de forma integral
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt

# Usando um modelo para melhor visualização
# processo chamado de cross validation
# processo de validação cruxada
# usada para quantidade de dados muito pequeno, e/ou, tornar o modulo mais robusto à partir dos dados q se tem
# modelo de predição, usando o conhecimento do modelo
# cv (cross validation)- número de partições
# ess eprocesos separa os dados em partições, sempre usando uma como teste e outras duas, no caso de treino
# a cada etapa, há alterações dos pedaços e suas posições


cv_results = cross_val_predict(clf, x_treino, y_treino, cv=3)
print(classification_report(y_treino, cv_results, target_names=categorias_gosta_futebol))

# Modelo gradico 1
fig, ax = plt.subplots()
ax.scatter(y_treino, cv_results, edgecolors=(0,0,0))
ax.plot([y_treino.min(), y_treino.max()], [y_treino.min(), y_treino.max()], 'k--', lw=4)
ax.set_xlabel('Real')
ax.set_ylabel('Predição')

plt.show()

# Plota matriz de confusão
from sklearn.metrics import plot_confusion_matrix

# Modelo gradico 2
plot_confusion_matrix(clf, x_treino, y_treino,
                      display_labels=categorias_gosta_futebol,
                      cmap=plt.cm.Blues,
                      normalize=None)

plt.show()

# Resultado:
# 1 - O modelo consegue identificar melhor aqueles que gsotam de futebol, do que os que não gostam
# após observar o valor mais elevado
# 2 - Análise gráfica, quanto mais longe da linha diagonal, mostra onde o modelo está errando,
# quanto mais perto da linha, mlehor acertebilidade

# -----------------------------------------------------------------------------------------------
# Modelo 03

# Análise à pártir da nacionalidade

atributos = ['idade', 'altura', 'peso', 'sexo','gosta de futebol', 'salario']

# processo de seleção, fatiamento do DataFrame
# porém pegando apenas todas as colunas passada na variável 'atributos'
# colocando dentro de um Data Frame 'df_clientes' e convertendo para numpy
x_treino = df_clientes.loc[:, atributos].to_numpy()

# Carregando a nossa variável indepednete
# vetor de caracteristicas(referência para comparação) de todos os clientes
# buscando a informação se p cliente gosta de futebol ou não
# y_treino = label (referência independente)
y_treino = df_clientes['nacionalidade'].to_numpy()

# Algoritnom de classificação
# classificador de árvore de decisão
# precisamos passar os criterios de divisão
# criterion = 'gini' - qual o indice que ele usa para fazer o processo de divisão na árvore
# splitter = 'best' - processo de divisão, com ele separa os ramos, as folhas da árvore
# max-depth - profundidade máxima que essa árvore vai atingir | 10 é pq temos 10 linhas no modelo
# min_samples_split - númeor mínimo de amostra para que se faça uma divisão
# max_features - máximo de atributos utilizados

clf=tree.DecisionTreeClassifier(criterion= "gini", splitter="best",
                                max_depth=5, min_samples_split=5,
                                min_samples_leaf=2, max_features=5)

# Processo de treinamento do modelo
# modelo de aprendizagem em sí
# .fit - processo de aprendizagem, de treinamento
clf = clf.fit(x_treino, y_treino)

# uso do graphviz

categorias_gosta_futebol = ['não gosta futebol', 'gosta futebol']
dot_data = tree.export_graphviz(clf, out_file=None, filled=True,
                                rounded=True,
                                special_characters=True,
                                feature_names=atributos,
                                class_names=['estrangeiro','brasileiro'])

graph = graphviz.Source(dot_data)
#graph.render("nacionalidade_tree") # salvando os dados em um arquivo
                            # debugou sem o .render
print(graph)
print("\n"*3)

# -----------------------------------------------------------------------------------------------
# Modelo 04

# divide os dados em treino e teste
from sklearn.model_selection import train_test_split
# permite tb fazer o processo de cross validation
from sklearn.model_selection import KFold

carros = pd.read_csv("carros_edit01_categororias.csv")
print(carros)
print("\n"*3)

# Seleciona apenas as colunas necessárias
# o label aqui, indica o modelo

x1 = carros.loc[:, 'ano':'preco_venda'].to_numpy()
y1 = carros['label'].to_numpy()

# info de conjunto de categorias:

len(np.unique(y1))
print("\n"*3)

# divide o conjunto em treinamento e teste, na proporção 80-20
# o que vamos utilizar para aprender
# o que vamos utilizar para testar

# train_test_split - devolve uma matriz, array numpy de todos os atributos de treino e testes
# test_size - a proporção que vai ficar para treino e para teste (0.25, significa 25% do total de dados)
# logo o de treino será 75%
# random_state - distribuição dos dados
# shuffle - embaralhamento dos dados

x1_treino, x1_teste,y1_treino, y1_teste = train_test_split(x1, y1, test_size=0.25,
                                                            random_state=123,
                                                            shuffle=True)
# fatiando os nomes das colunas
caracteristicas = list(carros.columns[2:-1])
carros['fabricante']= carros['fabricante'].astype('category')
# as categorias serão os nomes dos fabricantes
categorias = carros['fabricante'].cat.categories

print("Tamanho do conjunto de treinamento (75% do todo): {}\n".format(len(x1_treino)))
print("Tamanho do conjunto de testes (25% do todo): {}\n".format(len(x1_teste)))
print("Quantidade de características (qtd do vetor de caracteristica): {}\n".format(len(caracteristicas)))
print("Quantidade de classes ou categorias (qtd fabricantes): {}\n".format(len(carros['fabricante'].cat.categories)))

# Contando a quantidade de categorias de serviço
print("Nome do fabrincate e quantidade:\n")
categ_count= carros['fabricante'].value_counts()
print(str(categ_count))
print("\n"*3)

# Observando graficamente

categ_count.plot.bar()

# info das informações da colunas e não nulos e tipos de dados que eu tenho

print(carros.info())
print("\n"*3)

# processo de classificação utilizando o algoritmo de arvore de decisão
# definição do modelo
clf_carros=tree.DecisionTreeClassifier(criterion= "gini", splitter="best",
                                max_depth=3, min_samples_split=5,
                                min_samples_leaf=2, max_features=2)
# processo de treinamento
clf_carros_gini= clf_carros.fit(x1_treino, y1_treino)

# avaliando o desempenho do modelo treinado
# predição
# vai entregar um numero indicando qual é o fabricante
y_pred = clf_carros_gini.predict(x1_teste)

# comparação - Traz as categorias
# matriz de confusão é feita apenas com duas categoprias, neste caso, não trazer como o do exemplo do futebol que é binário a saida
# para resolver, pode olhar uma por vez.
# ou separar uma e comparar com as demais

plot_confusion_matrix(clf, x1_teste, y1_teste,
                      display_labels=categorias_gosta_futebol,
                      cmap=plt.cm.Blues,
                      normalize=None)

fig, ax = plt.subplots()
ax.scatter(y_treino, cv_results, edgecolors=(0,0,0))
ax.plot([y_treino.min(), y_treino.max()], [y_treino.min(), y_treino.max()], 'k--', lw=4)
ax.set_xlabel('Real')
ax.set_ylabel('Predição')