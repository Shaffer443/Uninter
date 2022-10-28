# Aula prática 02
# Premissa: Manipulação de numérica

import pandas as pd
import numpy as np




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

# Premissa de trabalhar com volume de dados grandes e dividir em várias matrizes
# numpy converte boa parte de listas trabalhadas em arrey, matrizese
# e essas arreys já são convertidas para trabalhar em altas dimenssões

# a ideia é entender como os dados estão armazenados

# array de 1 dimesão (axis)
# Transformando a lista em um obejto tipo array do numpy
array_1_dim = np.array([1,2,3])

# array de 2 dimesão (axis)

array_2_dim = np.array([[1,2,3],[4,5,6]])

# array de 3 dimesão (axis)
# podemos trablahr de forma intercambiada as listas e as tuplas
# poderia ser uma lista no lugar também

array_3_dim = np.array([[(1,2,3),(4,5,6)],[(1,2,3),(4,5,6)]])

# Verificando as dimensões dos arrays
# Explorando as informações:
# 1 - Informações do número de dimensões - .ndim
# 2 - seu formato. Numeor de linhas e colunas - .shape, informa (linhas, colunas)
# 3 - Qunatidade de elementos - .size
# 4 - Tipo armazeando dentro da matriz, arrey - .dtype

print("array_1_dim: {} dimensão / shape {} / {} elementos do tipo {}". format(array_1_dim.ndim,
                                                                              array_1_dim.shape,
                                                                              array_1_dim.size,
                                                                              array_1_dim.dtype))

print("array_2_dim: {} dimensão / shape {} / {} elementos do tipo {}". format(array_2_dim.ndim,
                                                                              array_2_dim.shape,
                                                                              array_2_dim.size,
                                                                              array_2_dim.dtype))

print("array_3_dim: {} dimensão / shape {} / {} elementos do tipo {}". format(array_3_dim.ndim,
                                                                              array_3_dim.shape,
                                                                              array_3_dim.size,
                                                                              array_3_dim.dtype))


print("\n")
print("-"*60)
print("\n")
# Demostração de rpocessos de manipulação através do vetor de caracteristicas

vetor_caracteristicas = [6,0,1,1,20,0,0,6]

vetor_numpy = np.array([6,0,1,1,20,0,0,6])

print("vetor_numpy: {} dimensão / shape {} / {} elementos do tipo {}". format(vetor_numpy.ndim,
                                                                              vetor_numpy.shape,
                                                                              vetor_numpy.size,
                                                                              vetor_numpy.dtype))

# Processo de mudança do formato
# em um vetor de 2 dimenssões, pratindo de um de uma dimensão
# reshape (4 - linhas, 2 - colunas)

vetor_numpy = vetor_numpy.reshape(4,2)
print("vetor_numpy: {} dimensão / shape {} / {} elementos do tipo {}". format(vetor_numpy.ndim,
                                                                              vetor_numpy.shape,
                                                                              vetor_numpy.size,
                                                                              vetor_numpy.dtype))

print("\n")
print("-"*60)
print("\n")

# Matrizes criadas pelo Numpy

# matrizes do tipo zerada, preenchidas com zero.
# defincninado apenas o tipo e o tamanho delas
# tupla definse o shape, o formato da matriz
# shape, determian a quantidade de elementos

array_1_dim_zeros = np.zeros(2, dtype=np.int32)
array_2_dim_zeros = np.zeros((3,2), dtype=np.int16)

print("array_1_dim_zeros: {} dimensão / shape {} / {} elementos do tipo {}". format(array_1_dim_zeros.ndim,
                                                                              array_1_dim_zeros.shape,
                                                                              array_1_dim_zeros.size,
                                                                              array_1_dim_zeros.dtype))

print("array_2_dim_zeros: {} dimensão / shape {} / {} elementos do tipo {}". format(array_2_dim_zeros.ndim,
                                                                              array_2_dim_zeros.shape,
                                                                              array_2_dim_zeros.size,
                                                                              array_2_dim_zeros.dtype))

print("\n")
print("-"*60)
print("\n")

# outros exemplos de matrizes que pode ser criadas
# preenchimentos automáticos

# contendo zeros
zeros = np.zeros(5)

# contendo somente 1 - ones
ones = np.ones((3,3))

# dentro de um intervalo arange
# definimos um range de 0 até 6, de 2 em 2
arange = np.arange(0,6,2)

# array vazio - empty
# sem valores definidos
empty = np.empty([2,2])

# linspace
# Informa um intervalo em uma quantidade de valores definidos
# intervalo de 1 ate 10, em 7 pedaços
# num - pedaços que será dividida o array
# pedaços uqalmente espaçados dentro do intervalo

linespace = np.linspace(1.0, 10.0, num=7)

# full
# matriz cheias
# cria uma matriz com um determiando valor
# tem sempe o mesmo valor colocado em todos so elemntos
# -2 = valor que será preenchido em todos os elementos

full = np.full((3,3,3), -2)

# indices
# ao inves de trazer os valores, ela irá trazer os indices
# quais os valores dos indices utilizados
# linha - coluna,e não os valores contidos

indices = np.indices((3,3))

print(f'Array de 0:\n{zeros}\n')
print(f'Array de 1:\n{ones}\n')
print(f'Array de entradas vazias:\n{empty}\n')
print(f'Array de intervalos:\n{arange}\n')
print(f'Array de espaçamento em um intervalo definido:\n{linespace}\n')
print(f'Array de indices:\n{indices}\n')

print("\n")
print("-"*60)
print("\n")
# ----------------------------------------------

# Outros exemplo, tipos de matrizes

# Matriz Diagonal
# Prenchida somente na diagonal principal ou não
diagonal = np.diag([1,2,3], k=0)

# Matriz identidade
# tera o seu valor todo com a diagonal principal 1 e o restante 0
identy = np.identity(3)

# matriz olho
eye = np.eye(4, k=0)

# Matriz aleatoria
# Para uso em teste ou seleção aleatória
rand = np.random.rand(3,2)

print(f'Matriz diagonal de estrutura semelhante a array:\n{diagonal}\n')
print(f'Matriz identidade:\n{identy}\n')
print(f'Matriz diagonal com 1\'s 0\'s:\n{eye}\n')
print(f'Matriz com números aleaórios:\n{rand}\n')

print("\n")
print("-"*60)
print("\n")
# ----------------------------------------------------------------

clienteref_01 = [22,0,1.70, 75,0,1,2500]

# verificando o tipo dos dados

type(todos_os_clientes)

# verificando o tipo dos dados do cliente_01

type(clienteref_01)

# Precisamos fazer um processo de conversão dos dados para uso

# Comparação do vetor de 1 cliente com todos os demais
# teremos todos os dados de clinete convertidos em um array -  array_todos
# PRocessando a conversão dos dados do clinete - array_cli01
# exemplo de comparação - array_comparacao
# comparando todos so clinetes com um cleiente expecifico, caso fosse o interesse.
# no numpy, podemos usar o broadcasting, que tem a premissa de pegar uma matriz e um vetor que é o cliente
# pegando toda a base de matriz e comparar com um cliente expecifico

# Neste exemplo abaixo, como seria feito, de fizemos uma matriz
# replicando 10x o cliente de referencia, cliente de referencia
# comparando o cliente de referÊncia com todos os outros

array_todos = np.array(todos_os_clientes) #convertendo os dados para um arrey numpy
array_cli01 = np.array([clienteref_01 for _ in range(array_todos.shape[0])]) # criamos um arrey numpy, repetindo 10x
array_comparacao = array_todos - array_cli01 #comparação é feita de forma direta, subtraindo da matriz gerada com todas as informações
                                                # o numpy já entende que ele precisa fazer isso linha a linha

# evitar que os numero sejam impresso em notação cientifica
np.set_printoptions(suppress=True)

# a ideia é de comparação
# seja comparação de salário, idade e qualquer uma das colunas
# se o resulatdo de comparação salarial for positivo, compárado com cliente de referencia
# indica que o salario é maior.
# e se for negativo é menor.
# lembrando que tudo comparado ao clinete de referência

# Exibindo informações

print("Comparação direta matriz x matriz")
print("Array de comparação: \n"+str(array_comparacao))
print("Formato do array_todos: {}".format(array_todos.shape))
print("Formato do array_cli01: {}".format(array_cli01.shape))

print("\n")
print("-"*60)
print("\n")

#-------------------------------------------------------------------------------------

# Usanodo o numpy briadcasting

# a premissa é a mesma do exemplo anterior
# porém, não precisou fazer o processo de criação da mariz de 10x do clinete de referência
# fazendo a conversão do cliente de referencia para um array numpy
# terá 10 dimensões, pois tem 10 clientes

# Compração por broadcasting
vetor_cli_01 = np.array(clienteref_01)
array_comparacao = array_todos - vetor_cli_01  # o numpy já entende que ele precisa fazer isso linha a linha


# exibe as informações

print("Comparação direta matriz x vetor")
print("Array de comparação: \n"+str(array_comparacao))
print("Formato do array_todos: {}".format(array_todos.shape))
print("Formato do vetor do cliente: {}".format(vetor_cli_01.shape))

print("\n")
print("-"*60)
print("\n")
# Busca o indice dos clientes com salário menor que o cliente de referência
# local do vetor para analise, do clinete de referencia  - vec[6]

idx_salario_menores = [idx for idx, vec in enumerate(array_comparacao) if vec[6] < 0]

print("\nIndice deos clinetes com o salário menos: {}".format(idx_salario_menores))

print("\n")
print("-"*60)
print("\n")
# indicando os indices para as informações do vetores de caracteristica com o salário menor
# que o clinete de referência
print("vetores dos clinetes com menor salário: {}".format(array_todos[idx_salario_menores]))



