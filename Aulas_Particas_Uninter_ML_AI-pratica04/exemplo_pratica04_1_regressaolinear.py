from sklearn import linear_model
from scipy.special import expit
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression #prediz uma classe
from sklearn.linear_model import LinearRegression # informa o valor categorigo
from matplotlib.collections import LineCollection
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import KFold
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Regressão Linear

# Nos permite trabalhar com informações que não categoricas
# Permite que trabalhemos com informações que não categoricas
# Consegue predizer um valor contínuio, como por exemplo, preço de venda.

# modelo de regressão tenta encontrar um reta, um modelo linear,
# que se aproxime de todos os pontos de todas as instancias.

# Ao ínvez de definirmos atricbutos, defincimos duas variáveis

# dataset
df_carros = pd.read_csv("carros_modelos_categorical.csv")

var1, var2 = ('popularidade', 'preco_venda')

df_2variaveis = df_carros.loc[:, [var1, var2] ]
#Tratamento que não recebe os dados repetidos
df_2variaveis = df_2variaveis.drop_duplicates(subset=var2, keep="last")
df_2variaveis = df_2variaveis.drop_duplicates(subset=var1, keep="last")

print('\n'*3)
print(df_2variaveis)

print('\n'*3)

# Plotagem 2:

x = df_2variaveis[var1].to_numpy()
y = df_2variaveis[var2].to_numpy()
n = len(df_2variaveis[var1])
lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)
y_= lr.predict(x[:, np.newaxis])

segments = [[[x[i], y[i]], [x[i], y[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(np.full(n, 0.5))

fig = plt.figure()
plt.plot(x, y, 'r.', markersize=8)
plt.plot(x,y_, 'b-')
plt.gca().add_collection(lc)
plt.legend(('Dados Reais', 'Predição'), loc='lower right')
plt.xlabel('Popularidade')
plt.ylabel('Preço de Venda')
plt.title('')
plt.show()

# COnsiderações para um carro ser popular ou não:
# Estamos considerando para que um carro seja popular ou não, os valores, tem que ser maior
# queo valor médio, com a informação 1, e caso não obdecer ao critério 0.
pop_media = df_carros ['popularidade'].mean()
df_carros['popular'] = np.where(df_carros['popularidade']> df_carros['popularidade'].mean(), 1, 0)

print(df_carros)
print('\n'*3)

#Classificação de automóveis em categorias: popular e não popular

carros =  df_carros.groupby("modelo").filter(lambda x: len(x) > 10)

#seleciona apenas as colunas necessárias:

carros['label'] = np.where(carros['popularidade']>carros['popularidade'].mean(), 1, 0)
y = carros['label'].to_numpy()

# apagando coluncas alvos:
carros = carros.drop(columns=['fabricante','modelo','popularidade'])
# Processo de fatiamento dos indices das colunas - Todos as linhas,execeto a ultima
x = carros.iloc[:, :-1].to_numpy()
# Processo de fatiamento dos indices das colunas - Todos as linhas,somente da ultima coluna
y = carros.iloc[:, -1].to_numpy()

# Divide o conjunto em treinamento e teste, na proporção 80-20

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.20,
                                                             stratify=y,
                                                             random_state=123,
                                                             shuffle=True)

# CLassificação Regressão Logistica
# C=le5 - declaração do modelo de regressão logistica
clf_logistica = linear_model.LogisticRegression()
#Execução do modelo
clf_logistica.fit(x_treino, y_treino)
y_pred_logistica = clf_logistica.predict(x_teste)

# Verificação do modelo treinado

# plota resultados

categorias = ['não popular', 'popular']
cv_results = cross_val_predict(clf_logistica, x_treino, y_treino, cv=3)

print("\n"*3)
print(classification_report(y_treino, cv_results, target_names=categorias))

fig, ax=plt.subplots()
ax.scatter(y_teste, y_pred_logistica, edgecolors=(0,0,0))
ax.plot([y_treino.min(), y_treino.max()],[y_treino.min(), y_treino.max()], 'k--', lw=4)
ax.set_xlabel('Real')
ax.set_ylabel('Predição')
plt.show()

# plota matriz de confusão

plot_confusion_matrix(clf_logistica, x_treino,y_treino,
                      display_labels=categorias,
                      cmap=plt.cm.Blues,
                      normalize=None)

plt.show()


