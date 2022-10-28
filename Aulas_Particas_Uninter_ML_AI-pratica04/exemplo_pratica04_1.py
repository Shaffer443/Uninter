# Executando a classificação para um conjunto maior de classes
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.metrics import (brier_score_loss, precision_score, recall_score, f1_score)
import pandas as pd
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB


# Processo predição, mudando a nossa etiqueta, alvo.
# Nossa categoria agora será tentar prevê o moodelo dele

column_label='modelo'

# Lê o dataset de carros

df_carros = pd.read_csv(f"carros_categorical.csv")
carros = df_carros.groupby("modelo").filter(lambda x: len(x)>10)

# Seleciona apenas as colunas necessárias
x = carros.loc[:, 'ano':'preco_venda'].to_numpy()
y = carros['label'].to_numpy()

# Divide o conjunto em treinametno e teste, na proporção 80-20

# o #stratify=y, apresentando erros,sem ele roda, com resulatdos discrepantes.
# Com ele, não roda o plot, dando divergências de valores de classes e o sistema pede para selecionar parâmetros

#Traceback (most recent call last):
#  File "C:\Users\shaff\PycharmProjects\aulas_uniter_ml_ai\Pratica_04\exemplo_pratica04_1.py", line 72, in <module>
#    resultados = classification_report(y_teste, y_predicao, target_names=code_cats, output_dict=True)
#  File "C:\Users\shaff\anaconda3\envs\aulas_uninter_ai\lib\site-packages\sklearn\metrics\_classification.py", line 2154, in classification_report
#    raise ValueError(
#ValueError: Number of classes, 390, does not match size of target_names, 382. Try specifying the labels parameter

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.20,
                                                             stratify=y,
                                                             random_state=123,
                                                             shuffle=True)

caracteristicas = list(carros.columns[2:-1])
carros ['modelo'] = carros ['modelo'].astype('category')
categorias = carros['modelo'].cat.categories

print("\n")
print("Tamanho do conjunto de treinamento: {}".format(len(x_treino)))
print("Tamanho do conjunto de teste: {}".format(len(x_teste)))
print("Quantidade de características (VC - Vetro de caracteristicas): {}".format(len(caracteristicas)))
#print("Quantidade de características: {}".format(len(carros['fabricante'].cat.categories)))
print("Quantidade de características: {}".format(len(categorias)))

# descrição de análise da colunad e fabricantes:
print('\n'*3)
print(carros['modelo'].describe())

# Treina um algoritmo de árvore de decisão com so dados

gnb = GaussianNB()
gnb.fit(x_treino, y_treino)

y_predicao = gnb.predict(x_teste)

print('\n'*3)
print("Total de classificações erradas de um total de {} instâncias: {}".format(x_teste.shape[0], (y_teste != y_predicao).sum()))

# Avalia o desempenho do modelo treinado

print('\n'*3)
print("Total de categorias: {}".format(len(categorias)))

cats_teste = np.unique(y_teste).tolist()
code_cats = carros['modelo'].cat.categories

print("Total de categorias de teste: {}".format(len(code_cats)))
print('\n'*3)

resultados = classification_report(y_teste, y_predicao, target_names=code_cats, output_dict=True)

# Plota o grafico de resultados
# Graficos simplificados

fig, ax = plt.subplots()
ax.plot([y_teste.min(), y_teste.max()],[y_teste.min(), y_teste.max()], 'k--', lw=2, color='red')
ax.scatter(y_teste, y_predicao, edgecolors=(0,0,0))
ax.set_xlabel('Real')
ax.set_ylabel('Predição')
plt.show()

# Quando o resulatdo é muito disperso, não é tão bom
# temos a opção de melhorar com a calibração

# Metodo isotonico
isotonic = CalibratedClassifierCV(gnb, cv=4, method='isotonic')

# Metodo sigmoid
sigmoid = CalibratedClassifierCV(gnb, cv=4, method='sigmoid')

isotonic.fit(x_treino, y_treino)
sigmoid.fit(x_treino, y_treino)

predicoes = [p.predict(x_teste) for p in [gnb, isotonic, sigmoid]]

for y_predicao in predicoes:
    print("Total de classificações erradas de um total de {} instâncias: {}".format(x_teste.shape[0],(y_teste != y_predicao).sum()))
    print("\nPrecisão: %1.3f" % precision_score(y_teste, y_predicao, average='macro'))
    print("\nRecall: %1.3f" % recall_score(y_teste, y_predicao, average='macro'))
    print("\nF1: %1.3f" % f1_score(y_teste, y_predicao, average='macro'))

    #Devolve um lista de predições com valores
    resultados = classification_report(y_teste, y_predicao, target_names=code_cats)

    # Plota o grafico de resultados
    # Graficos simplificados

    fig, ax = plt.subplots()
    ax.plot([y_teste.min(), y_teste.max()], [y_teste.min(), y_teste.max()], 'k--', lw=2, color='red')
    ax.scatter(y_teste, y_predicao, edgecolors=(0, 0, 0))
    ax.set_xlabel('Real')
    ax.set_ylabel('Predição')
    plt.show()



