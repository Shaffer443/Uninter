# Aula 05 | Exercício 01

# Escreva uma rotina que crie uma borda ao redor de uma palavra para destaca-la
# como sendo titulo.
# A rotina deve receber como parâmetro a palavra a ser destacada.
# O tamanho da caixa de texto deverá ser adpatável de acordo com o tamanho da palavra.

def texto():
    nome = input('Digite uma palavra: ')
    letras = len(nome)
    print('+','-' *letras,'+')
    print('|', nome, '|') # pode-se chamar uma variável direto. no caso NOME
    print('+','-' *letras,'+')

# Chamando Função

texto()