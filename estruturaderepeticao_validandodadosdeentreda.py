# Validando Dados de Entrada

# criando regras para valores de entradas

# exemplo 1:

# Receber um valor do tipo inteiro vai teclado
# O programa so deve aceitar, obrigatoriamente valores inteiros e positivos
# qualquer valor negativo ou igual a zero, deve ser rejeitado pelo programa
# e um novo valor deve ser solicitado.

# Validando Entrada:

x = int(input('Digite um valor maior que zero: '))
while(x <= 0):
    x = int(input('Digite um valor maior que zero: '))
print('Voce digitou %i. Encerrando o programa...' %x)

# instrução break:

print('\n')
# Receber palavras e frases digitadas pelo usuário
# encerre o algoritmo quando a palavra "sair" for digitada

while (True): # Apenas fica reperindo, sem parametros definido
    frase = input('Digite uma frase ou palavra: ')
    print(frase)
    if(frase == 'sair'):
        print('Você digitou SAIR. Encerrando o programa...')
        break # encerra o laço while

# instrução break:

print('\n')

# escreva um algoritmo que realize um login em um sistema
# o usuário deve informar seu nome e senha.

while (True):
    login = input('Digite o seu login: ')
    if(login != 'shaffer'):
        continue
    senha = input('Digite sua senha numérica: ')
    if(senha == '019652'):
        break
print('Acesso Permitido!')
