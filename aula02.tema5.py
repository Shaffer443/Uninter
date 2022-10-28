# Pergunta uma entreda via teclado ( input == scanf ) #

nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')
print('Seu nome é {}. Sua idade é {}.'.format(nome, idade)) # Precisa de um parentese apra informar corretamente um input #
tamanho = len(nome)
print ('seu nome tem %i caractere(s)'% tamanho)

# Convertendo dados de Entrada #

nota = float(input('Qual foi a sua nota? '))
print('Sua nota foi {}'.format(nota))

# Exercício - Desenvolva um algoritmo que solicite ao usuário dois números inteiros. imprima a soma destes dois números na tela #

n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
soma = n1 + n2
print('A soma dos dois números é: %i'% soma) # maneira clássica
soma2 = 'A soma de {} e {} é: {}'.format(n1, n2, n1+n2) #maneira moderna
print(soma2)