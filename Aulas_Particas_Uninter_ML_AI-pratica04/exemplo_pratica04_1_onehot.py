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


# Classificação de automoveis em categorias: popular e não-popular

# dataset
df_carros = pd.read_csv("carros_modelos_categorical.csv")
#Classificação de automóveis em categorias: popular e não popular
carros =  df_carros.groupby("modelo").filter(lambda x: len(x) > 10)
#seleciona apenas as colunas necessárias:
carros['label'] = np.where(carros['popularidade']>carros['popularidade'].mean(), 1, 0)
y = carros['label'].to_numpy()


# usando one-hot encoder - que se converte a categoria em números
# onde cada categoria e um atributos
# e esses atributos, apenas uma tem o valor 1. Trazendo separabilidade das instâncias

# tem a vantagem de é que ele pode, a aprtir de um processo de codificação
# trará um resulatdo mais preciso. Faz uma busca melhor, e o modelo aprende melhor

# Dados transformado em hot one:
carros= pd.concat([pd.get_dummies(carros['tipo_transmissao'], prefix='tipo_transmissao', drop_first=True),
                           pd.get_dummies(carros['tracao'], prefix='tracao', drop_first=True),
                          pd.get_dummies(carros['combustivel'], prefix='combustivel', drop_first=True),
                          pd.get_dummies(carros['tamanho'], prefix='tamanho', drop_first=True),
                          pd.get_dummies(carros['estilo'], prefix='estilo', drop_first=True),
                          carros], axis=1)

carros = carros.drop(columns=['fabricante', 'modelo', 'popularidade', 'tipo_transmissao','tracao',
                              'combustivel', 'tamanho', 'estilo', 'preco_venda'])

# Processo de fatiamento dos indices das colunas - Todos as linhas,execeto a ultima
x = carros.iloc[:, :-1].to_numpy()
# Processo de fatiamento dos indices das colunas - Todos as linhas,somente da ultima coluna
y = carros.iloc[:, -1].to_numpy()

# Divide o conjunto em treinamento e teste, na proporção 80-20
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.20,
                                                             stratify=y,
                                                             random_state=123,
                                                             shuffle=True)

# Classificação Regressão Logistica
# C=le5 - continua dando problema apra reconhecimento do parâmetro
clf_logistica = linear_model.LogisticRegression(max_iter=10000, class_weight={0:0.7,1:0.9})
clf_logistica.fit(x_treino, y_treino)
y_pred_logistica = clf_logistica.predict(x_teste)

print('\n'*3)
print(carros)

