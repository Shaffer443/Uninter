# Escreva uma função para validar uma string.
# Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo,
# e falso, caso contrário.

def validar(escrita, min, max): # usando como referência x, y e z. porem cabe qualquer coisa
    string = input(escrita) # pegará o parâmetro x,que nesse caso é 'escrita'. relaciona o input ao escrita(x)
    caracteres = len(string) # contará os caracteres da escrita == string

    while((caracteres<min) or (caracteres>max)): # laço de validação. Se a string = escrita estiver fora dos parâmetros de min = 10 e max = 30
        string = input(escrita) # o que o WHILE perguntará novamente caso estja fora dos parâmetros minimos e máximos definidos
        caracteres = len(string)
    return string

# Programa Principal (Global puxando da função)

resultado = validar('Digite: ', 10, 30) # usei 'Digite:', para ser a variável X (na nossa alusão), porém, através de um pergunta.
print('Você digitou a string: {}. Está entre os parâmetros aceitos.'.format(resultado))

# podemso também trabalhar para que as variáveis 10 (equivalente a y) e 30 (equivalente a z),
# sejam perguntados ao usuário, oa ínves de ser declarado como no exercício.