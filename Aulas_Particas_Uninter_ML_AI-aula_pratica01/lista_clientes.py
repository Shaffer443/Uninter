# Disciplina Machine Learning
# Aula prática 01 -  Conceitos Básicos

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

# Modelo não recebe outra informação que não é nuemros.
# Não se pode usar textos dentro do smodelos, espera sempre números.
# Precisamos converter as informações

# Vetores de caracteristicas dos clientes:

caracteristicas_cliente_01 = [38,0,1.74,80,0,1,0]
caracteristicas_cliente_02 = [6,0,0.40,12,0,0,0]
caracteristicas_cliente_03 = [19,0,1.70,60,1,1,0]
caracteristicas_cliente_04 = [26,0,1.70,60,1,0,0]

# Exibindo os clientes e os seus vetores de características

def info_clientes():
    print("\nCliente 01: "+str(cliente_01))
    print("Vetor de Características do Cliente 01: "+ str(caracteristicas_cliente_01))

    print("\nCliente 02: "+str(cliente_02))
    print("Vetor de Características do Cliente 02: "+ str(caracteristicas_cliente_02))

    print("\nCliente 03: "+str(cliente_03))
    print("Vetor de Características do Cliente 03: "+ str(caracteristicas_cliente_03))

    print("\nCliente 04: "+str(cliente_04))
    print("Vetor de Características do Cliente 04: "+ str(caracteristicas_cliente_04))

# principal | executáveis
# funções:

info_clientes()