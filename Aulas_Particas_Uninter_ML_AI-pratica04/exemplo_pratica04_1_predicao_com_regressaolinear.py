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
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Modelo de predição usando regressão linear:
# Da para se usar tanto para calissicar categorias quanto para predição de valores continuos

# dataset
carros = pd.read_csv("carros_modelos_categorical.csv")

#seleciona apenas as colunas necessárias:
x=carros.loc[:, 'ano':'popularidade'].to_numpy() #.reshape(-1,1)
y=carros['preco_venda'].to_numpy() # referÊncia

#Divide o conjunto em treinametno e teste, na proporção 80-20
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.30)

#Classificação regressão linear
ols = linear_model.LinearRegression(normalize=True)
ols.fit(x_treino, y_treino.reshape((-1, 1)))
y_pred_ols = ols.predict(x_teste)

print('\n'*3)
print('Coeficiente: \n', ols.coef_)
print('Coeficiente de Determinação: %.2f' % r2_score(y_teste, y_pred_ols))

# plota resultados:

fig, ax=plt.subplots()
ax.scatter(y_teste, y_pred_ols , color='red', edgecolors='black')
ax.scatter(y_teste, y_teste, color='green', edgecolors='black')
ax.set_xlabel('Real')
ax.set_ylabel('Predição')
plt.legend(('Valores de PRedição', 'Valores Reais'), loc="best", fontsize='medium')
plt.show()

# A comparação será um pouco diferente, pois o valor predito, como é continuo, oq ue podemos fazer éc omparar diferneça
# do valor.
# Não temos categorias
# mas podemos comparar com o coeficientes
# mas ele não é acuraccy
