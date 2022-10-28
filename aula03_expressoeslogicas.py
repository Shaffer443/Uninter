# Expressões Lógicas e Álgebra Booleana

# not

x = True
y = False

print(not x)
print(not y)

# exercício 1:

a = 10
b = 1
res1 = not a > b
# primeiro o sistema faz a comparaçao, e só depois ele nega, invertendo o resultado
print(res1)

# resultado inverterá as situações/opções

# and

x = True
y = False
print('\n')
print( x and y)

# exercício 2:

c = 10
d = 1
e = 5.5
res2 = c > d and e == d
# 1 - c > d ( 10 > 1 == v)
# 2 - e == d ( 5.5 == 1 == f)
# 3 - and == v + f == f
print(res2)

# or

x = True
y = False
print('\n')
print(x or y)

# exercício 3:

# um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando.
# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
# Escreva um algoritmo que leia a nota final do aluno em cada matéria e informe, na tela, se ele passou ou não.

materia1 = float(input('Digite a Primeira nota: '))
materia2 = float(input('Digite a Segunda nota: '))
materia3 = float(input('Digite a Terceira nota: '))

soma = materia1+materia2+materia3
print('\n')
if (soma>21):
    print('Aluno Aprovado! Parabéns')
else:
    print('Aluno está Reprovado.')