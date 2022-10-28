# Exercício 01

# Faça um algoritmo que receba três valores, representando os lados de um truângulo
# fornecidos pelo usuário. Verifique se os valores forma um triângulo e classifique como:

 # a) Equilátero ( três lados iguais)
 # b) Isósceles ( dois lados iguais)
 # c) Escaleno ( três lados diferentes)
 # d) Nenhum lado pode ser igual a zero
 # e) Nenhum lado pode ser maior do que a soma dos outros dois

a = int(input('Digite um valor para o Primeiro lado: '))
b = int(input('Digite um valor para o Segundo lado: '))
c = int(input('Digite um valor para o Terceiro lado: '))

if(a==0 or b==0 or c==0):
    print('Não podemos formar um triangulo com um valor zero(0).')
elif(a+b<c or c+b<a or c+a<b):
    print('Um lado não pode ser maior do que a soma dos outros dois.')
elif(a == b == c):
    print('Este triângulo é EQUILÁTERO ( três lados iguais)')
elif(a==b!=c or b==c!=a or c==b!=a):
    print('Este triângulo é ISÓSCELES ( dois lados iguais)')
elif(a!=b!=c):
    print('Este triângulo é ESCALENO ( três lados diferentes)')
