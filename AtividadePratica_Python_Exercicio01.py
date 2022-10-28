# Exercício 01

# A ampliação do Ensino Fundamental para nove anos de duração, tornou a matricula da criança
# obrigatória a partir dos seis anos de idade. Implemente um programa que fornecidos
# o nome e a idade de uma criança, classifique-a em uma das seguintes etapas de ensino:

# Educação Infantil - 1 a 5 anos.
# Ensino Fundamental I - 6 a 10 anos.
# Ensino Fundamental II - 11 a 14 anos.
# Ensino Médio - Maiores de 15 anos.

# O usuário deve ainda ter a opção de escolher se quer encerrar o programa ou não.
# Para teste como nome da criança o seu nome e como idade os dois últimos dígitos de RU.


print('Programa de Verificação de Enquadramento de Ensino\n')


# Criei um função única para chamar os inputs dos dois dados das variáveis (Nome e idade).
# Criei IF e ELIF's para os parâmetros de cada faixa de ensino, conforme enunciado.

def verificacao():

    nome = input("Digite seu Nome: ")
    idade = int(input("Digite sua Idade: "))
    print('\nNome do Aluno(a): {}'.format(nome))
    print('Idade do Aluno(a): {}'.format(idade))
    if(idade >= 1 and idade <= 5):
        print('A aluno(a) {} tem {} anos e está na Educação Infantil.'.format(nome, idade))
    elif (idade >= 6 and idade <= 10):
            print('A aluno(a) {} tem {} anos e está na Ensino Fundamental I.'.format(nome, idade))
    elif (idade >= 11 and idade <= 14):
            print('A aluno(a) {} tem {} anos e está na Ensino Fundamental II.'.format(nome, idade))
    elif (idade >= 15):
            print('A aluno(a) {} tem {} anos e está na Ensino Médio.'.format(nome, idade))

# Aqui chamo a função criado acima.
verificacao()

# Criei uma variável do tipo inteira para o questionamento sobre o encerramento ou não do programa.
res = int(input('\nDeseja Continuar? 0 - Não   1 - Sim: '))

# Criei um laço While para continuar executando o programa, caso não seja encerrado.
while(res == 1):
 verificacao()
 res = int(input('\nDeseja Continuar? 0 - Não   1 - Sim: '))

# finalizando o programa caso saia do laço while.
print("Finalizando Programa. Fechando programa... ")


