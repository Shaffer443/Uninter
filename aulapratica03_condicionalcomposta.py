# Condicional Composta

# Traduza as afirmações a seguir para condicionais em Python:

# a) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um ano bissexto"
# b) Se ambas as variáveis booleanas Cima e Baixo forem True, escreva: "Decida-se!", caso contrário, escreva: "Você escolheu um caminho!"

# a)

ano = int(input('Digite o ano: '))
bissexto = ano % 4

if(bissexto == 0):
    print('Pode ser um ano Bissexto.')
else:
    print('Definitivamente não é um ano Bissexto.')

# b)

# nesta questão precisa-se criar as variáveis, onde não criei pela questão não solicitar isso. Apenas armar

if(cima or baixo): # cima == True ou cima, é a mesma coisa
    print('Decida-se!')
else:
    print('Você escolheu um caminho..')