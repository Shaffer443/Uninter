# Aula 02 - Pratica 02

# Expressões Algébricas

# Escreva as seguntes expressões algébricas em linguagem python:

    # a) o somatório dos 5 primeiros números interiores e positivos
    # b) A média entre 23,19 e 31
    # c) O número de vezes que 73 cabe em 403
    # d) A sobra quando 403 é dividido por 73
    # e) 2 elevado à 10 potencia
    # f) o valor absoluto da diferença entre 54 e 57
    # g) O menor valor entre 34,29 e 31

# a)

a = 1 + 2 + 3 + 4 + 5
print(a)

# b)

n1 = 23
n2 = 19
n3 = 31
mediab = (n1 + n2 + n3 )/3
print(mediab)

# c)

n4 = 73
n5 = 403
c = n5 // n4
print(c)

# d)

d = n5 % n4
print(d)

# e)

e = 2 ** 10
print(e)

# f)

# usar abs() que pega o valor absoluto

f = abs(54 - 57)
print(f)

# g)

# podemos encontrar o menor valor usando o recurso min()

print(min(34,29,31))

# usando resultado resumido em uma linha. Poderia ter feito assim para as demais questões.


# Atribuição

    # a) Atribuir o valor inteiro 3 à variável 'A'
    # b) Atribuir o valor 4 à variável 'B'
    # c) Atribuir à variável 'C" o valor da expressão a*a + b*b

# a)

A = 3

# b)

B = 4

# c)

print((A*A + B*B))

#strings

# Execute as seguintes atribuições

    # a) s1 = 'ant'
    # b) s2 = 'bat'
    # c) s3 = 'cod'

# a)

s1 = 'ant'

# b)

s2 = 'bat'

# c)

s3 = 'cod'

#Agora, utilizando operadores + e *, crie as saídas a seguir:

    # a) 'ant bat cod'
    # b) 'ant ant ant ant ant ant ant ant ant ant'
    # c) 'ant bat bat cod cod cod'
    # d) 'ant bat ant bat ant bat ant bat ant abt ant abt ant bat'
    # e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

#obs: para adionar um espaço em branco adicione + ' ' + antes da concatenação

# a)

print( s1 + ' ' + s2 + ' ' + s3)

# b)

print((s1 + ' ') * 10)

# c)

stringc2 = (s2+ ' ')*2
stringc3 = (s3 + ' ')*3

print( s1 + ' ' + stringc2 + stringc3)

# d)

stringsd = s1 + ' ' + s2 + ' '
print( stringsd * 7)

# e)

stringse = s2+s2 + s3 + ' '
print(stringse * 5)

# Exercício 1

# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# calcule e exiba o valor do desconto e o preço final do produto ( exercícío da apsotila - aula 2).

preco = float(input('Qual o preço do produto: '))
desconto = float(input('Qual é o desconto? (0 - 100): '))
precodesconto = preco * (desconto / 100)
precofinal = preco - precodesconto
print('Desconto de R$ {}, {} % de desconto. preço final de R$ {}'.format(precodesconto, desconto, precofinal))

# Exercício 2

#Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuário,
#assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

kmpercorrido = float(input('Quantos quilometros foi utilizados? '))
diasalugados = int(input('Quantos dias o veículo ficou alugado? '))
precodia = 60.00
precokm = 0.15

custodias = precodia * diasalugados
custokm = precokm * kmpercorrido

print('Custo das diárias R$ {} + Km utilizados R$ {}. Valor total à pagar R$ {}'.format(custodias, custokm, custodias+custokm))

# Exercício 3

#Crie uma variável de string que receba uma frase qualquer.
#Crie uma segunda variável, agora contendo a metade da string digitada.
#imprima na tela somente os dois últimos caracteres da segunda variável do tipo string.

string = input('Escreva sua frase: ')
tamanho = len(string) # pega quantidade de caracteres
string2 = string[:int(tamanho/2)] # pegando a ultima metade, tem que colocar 'int' por querer inteiro (não pode cortar uma metade da letra
print('O ultimos caracteres da segunda string é: {}'.format(string2[-2:]))

#obs1: se colocar menos no indice significa que ele vao contar da direita para esquerda. Ex [-2:]