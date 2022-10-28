# Exercício 2
# Transformar para maiúscula. Modificar as vogais em uma frase ou palavra, para os caracteres abaixo:

# A = @
# E = &
# I = !
# O = #
# U = *

print('## Codificação de Vogais ##\n')

# Solicita ao usuário a inserção de uma frase ou palavra
nome = input('Digite um Nome ou Frase: ')
# Transforma a string digita para maiúsculo
nometransf = nome.upper()
# Imprime a variável transformada.
print('Convertendo palavra(as) ou frase para maiúsculo: {}'.format(nometransf))

# Criei uma variável 1 para que possa verificar se possui a "A" na palavra ou frase já em maiúsculo.
# Se sim, será modificada.
nometransfA = nometransf.replace('A','@')
# Criei uma variável 2 para que possaar a primeira variável verificadora (variável 1) e verifica se possui a vogal "E" também na palavra ou frase.
# Se sim, será modificada.
nometransfE = nometransfA.replace('E','&')
# Criei uma variável 3 para que possaar a primeira variável verificadora (variável 2) e verifica se possui a vogal "I" também na palavra ou frase.
# Se sim, será modificada.
nometransfI = nometransfE.replace('I','!')
# Criei uma variável 4 para que possaar a primeira variável verificadora (variável 3) e verifica se possui a vogal "O" também na palavra ou frase.
# Se sim, será modificada.
nometransfO = nometransfI.replace('O','#')
# Criei uma variável 5 para que possaar a primeira variável verificadora (variável 4) e verifica se possui a vogal "U" também na palavra ou frase.
# Se sim, será modificada.
nometransfU = nometransfO.replace('U','*')

# Imprime o resultado de ultima variável após passar por todas as verificações das vogais, contidas ou não na frase ou palavra.
print('Trocando as vogais da palavra ou frase pelos caracteres especiais: {}'.format(nometransfU))
