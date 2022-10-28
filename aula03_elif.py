# Condicional de Multipla Escolha

# exercício 1:

print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual Fruta você escolhe? (1,2 ou 3): '))
quantidade = int(input('Qual a quantidade? '))

if (produto == 1):
    pagar = quantidade * 2.3
    print('Você comprou {} maça(s). Valor Total à pagar R$ {}' .format(quantidade, pagar))
elif(produto == 2):
        pagar = quantidade * 3.6
        print('Você comprou {} Laranja(s). Valor Total à pagar R$ {}'.format(quantidade, pagar))
elif(produto == 3):
            pagar = quantidade * 1.85
            print('Você comprou {} Banana(s). Valor Total à pagar R$ {}'.format(quantidade, pagar))
else:
    print('Produto Inexistente.')

# pedir a quantidade ficou irrelevante no ultimo else. porém, faz a função rodar.

# exercício 2

# Escreva um algoritimo que lê um nome e uma idade.
# Caso o nome digitado seja Rafael ou rafael, Escreva isso na tela.
# Caso contrário, verifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for maior que 100,
# informe que esta pessoa é muito idosa ou não existe.

nome = input('Escreva seu nome: ')
idade = int(input('qual a sua idade? '))

print('\n')

if(nome == 'Rafael' or nome == 'rafael'): # condicional de string, usar '' simples
    print('Seja bem Vindo {}'.format(nome))

elif(idade < 18):
    print('Você não é Rafael,e é de menor.')
elif(idade > 100):
    print('Você não é Rafael, e tem uma idade muito avançada ou Falecido')


