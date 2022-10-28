# Estudando função com parâmetro

# criando função
def titulo(nome): # entre parêntese se pode colcoar uma váriavel
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')
    print(nome)
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')

# chamando a função

titulo( nome=input('Digite um nome: '))
#dentro da variável na função, chamo ela, onde a função em pergunta o q colcoar na variável.


# Outra maneira de se solicitar uma variável dentro de uma função. passar parâmetros

# criando função
print('\n')

def soma ():

    n1 = int(input('Insira um número inteiro: '))
    n2 = int(input('Insira um número inteiro: '))
    calc = n1 + n2
    print(calc)

# chamando a função

soma()

# criando função com parâmetros definidos

print('\n')

def substracao (x, y):
    res=(x-y)
    print(res)

#chamando função, qunatas vezes quiser

substracao(10, 30)
substracao(10, 15)

# posso alterar as possições de X e Y, em seus valores, explicitando-os

substracao(y=8, x=12)