# Retorno de Valores em Função

print('Exemplo 1:\n')

def soma(x=0, y=0,z=0):
    res=x+y+z
    return res

# Programa Principal

retornado = soma(1,2,3)
print(retornado)

# Forma alternativa simplificada

print(soma(2,2)) # Juntando as funções. 1 - ele faz a soma e depois o print

print('\nExemplo 2:\n')

retornado1 = soma(4,5,6)
retornado2 = soma(4,5)
retornado3 = soma()

# pode-se aproveitar os resultados guardados nas variáveis e usar posteriormente.

print('Somatorios: {}, {}, {}' .format(retornado1, retornado2, retornado3))
