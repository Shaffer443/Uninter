# Um número de variáveis de clientes maiores, para se analisar resulatdos e análises com pandas

# Focando em vetores de características
# Indica como são as instâncias
# e tem as etiquetas, caracyterizando as etiquetas, com as infromações dos dados analisados

import pandas as pd

# Caracteristicas numéricas convertidas:

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

# Usando o objeto de trabalho principal do pandas, chamado Data Frame
# Utliza números, mas também informações não numericas,
# mas podemos definir as colunas e as informações que cada ponto numérico esta representando

df_clientes = pd.DataFrame(data=todos_os_clientes,columns=[
    "Idades",
    "Nacionalidade",
    "Altura",
    "Peso",
    "Gênero",
    "Gosta de Futebol?",
    "Salario"
])

# Há colunas já transformadas em processos de categorização: 0 - brasileiro, 1 - estrangeiros.

# exibir objetos do pandas para por o nome da variável que se deseja,quando não se usa IDE (jupyter, colab, outros)

df_clientes
print(df_clientes)

## Agora trabalhar o processo de visualização dos dados ##

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Criando uma lista de de associação de valores das nacionalidades
# e associamos cores a elas
# a premissa é separar os dados dos clientes gostam ou não de futebol

gosta_futebol = ["Não gosta de futebol", "GOSTA de futebol"]
cores = ['red','blue']

# Chamada das definições do gráfico
# desenha o gráfico para cada categoria

plt.figure(figsize=(16,10), dpi=80, facecolor='w', edgecolor='k')

# trazer a informação das idades,e no processo, na busca dentro dos dados de clientes
# buscando por meio de um processo de interação de cada linha, pegandono a primeira coluna de cada linha
# estamos interando todos os clientes, pegando cada linha e a primeira coluna de cada linha obdecendo um criterio
# passando pelas duas possibilidades de nacionalidades
# onde cada uma delas, filtrar, mostrando para cada uma das opções
# idades e salarios, colocando-as em um gráfico

# dados_cleinte[x] - passado a informação da coluna onde queremso pegar os dados
# enumerate(z) - informamos qual a coluna alvo para premissa da análise.
# no caso aqui a coluna com so dados do gosto True, false sobre futebol.
# informaremos também, na ultimo dados_clientes[x], a localização da informação alvo.
# no caso, será a "Gosta de Futebol?" = [5] * Maior mudança, a da coluna
# label alterado de str(nac) -> para str(g)

for i, nac in enumerate(gosta_futebol):
    idades = [dados_cliente[0] for dados_cliente in todos_os_clientes if dados_cliente[5]==i]
    salarios = [dados_cliente[6] for dados_cliente in todos_os_clientes if dados_cliente[5]==i]
    plt.scatter(idades, salarios, s=30,c=cores[i], label=str(nac))

### Adcionanedo o apontamento de Outlier nos resultados gráficos:

plt.annotate('Outlier', xy=(49, 25000), xytext=(40,26000),
             arrowprops=dict(arrowstyle="->", facecolor='black',
             connectionstyle="arc3"))

# Ajuste no layout
# alterados:
# xlim=(0,100) - > (0,80)
# titulo para: "Distribuição dos Gosto por Futebol por Idade e Salário"

plt.gca().set(xlim=(0, 80), ylim=(0,30000),
              xlabel='Idade', ylabel='Salário')
plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Distribuição dos Gosto por Futebol por Idade e Salário", fontsize=18)
plt.legend(fontsize=18)
plt.show()

# Resultados:
# Clinete = Istância
# Outilier = InstÂncia ou conjunto de instÂncia que destoa dos demais resultados