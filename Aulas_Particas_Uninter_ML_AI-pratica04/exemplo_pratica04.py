# Disciplina Machine Learning
# Aula 04 - Apredizagem Supervisionada - Parte II
# Classificação Supervisionada
# Classificador Bayesiano (Naive Bayes)

# Processo predição, mudando a nossa etiqueta, alvo.
# Nossa categoria agora será tentar achar o fabrincate á partir dos dados.

import matplotlib.pyplot as plt # Faz o processo da plotagem dos dados
import pandas as pd

# Teorema de Bayes aplicado de dados de clientes
# Podemos avaliar as probabilidade de categorias, de acordo com os atributos cujos valores conhecemos.

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# lê o dataset carros:
carros = pd.read_csv(f"carros_edit02_categororias.csv")

# Seleciona apenas as colunas necessárias:

# fatiando o DF e selecionando os atributos das colunas do "ano" até "preco de vendas"
x = carros.loc[:, 'ano':'preco_venda'].to_numpy()
# fazendo a seleção da variável independente da categoria, a etiqueta
# caso desta 'label' é cada carro
y = carros['label'].to_numpy()

# Divide o conjunto em treinamento e teste, na proporção 80-20:
# stratify=y - a ideia é que o processo de divisão garanta que teremos elementos
# de todas as categorias de treinamento no teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.20,
                                                             #stratify=y,
                                                             random_state=123,
                                                             shuffle=True)

caracteristicas = list(carros.columns[2:-1])
carros ['fabricante'] = carros ['fabricante'].astype('category')
categorias = carros['fabricante'].cat.categories

print("\n")
print("Tamanho do conjunto de treinamento: {}".format(len(x_treino)))
print("Tamanho do conjunto de teste: {}".format(len(x_teste)))
print("Quantidade de características (VC - Vetro de caracteristicas): {}".format(len(caracteristicas)))
#print("Quantidade de características: {}".format(len(carros['fabricante'].cat.categories)))
print("Quantidade de características: {}".format(len(categorias)))

# descrição de análise da colunad e fabricantes:
print('\n'*3)
print(carros['fabricante'].describe())

#print('\n'*3)
#print(carros['tracao'])

# fazendo utilização do algoritmo bayesiano com so dados
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_treino, y_treino)

y_predicao = gnb.predict(x_teste)
print('\n'*3)
print("Total de classificações erradas de um total de {} instâncias: {}".format(x_teste.shape[0], (y_teste != y_predicao).sum()))

# informa como o resultado, qual o nome do fabricante do carro, onde ele erra em não acertar predizer o fabricante carro
# partindo do vetro de caracteristicas (vc) de atriutos daquele carro.

# Avalia o desempenho do modelo treinado
import numpy as np
from sklearn.metrics import classification_report

# Traz informações de como a clasficação e processo de predição e comportou se comportou
# o quanto se conseguiu acertar.

print('\n'*3)
print("Total de categorias: {}".format(len(categorias)))

cats_teste = np.unique(y_teste).tolist()
code_cats = carros['fabricante'].cat.categories
print("Total de categorias de teste: {}".format(len(code_cats)))

# Plotando o grafico de resultados:

fig, ax = plt.subplots()
ax.plot([y_teste.min(), y_teste.max()],[y_teste.min(), y_teste.max()], 'k--', lw=2, color='red')
ax.scatter(y_teste, y_predicao, edgecolors=(0,0,0))
ax.set_xlabel('Real')
ax.set_ylabel('Predição')
plt.show()

# o grafico nos mostra qualitativamente e não quantitativamente.
# Dentro da linha, acertos, fora, erros de qualificação, que o modelo consegue acertar com os testes
# quanto mais distante, maior a quantiodade de erros
# quanto mais perto, menor

# Resultado partindo do relatório de qualificação:

relatorio =  classification_report(y_teste, y_predicao, target_names=code_cats)

print('\n'*3)
print(str(relatorio))

# Informa:
# - Resultado 1.00 - o modelo aprendeu bem.
# - Abaixo disso, pode-se melhorrar ou não.
# accuracy - médias

