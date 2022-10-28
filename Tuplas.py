# Construindo e Manipulando Tuplas

# Representado entre parênteses ()
# Estrutura estática
# é imutável

# Indices:    0          1         2         3
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
# Assim que você coloca os dados entre parênteses(),
# o python já reconhece que mochila é uma tupla

# Mostrará todos os dados de Mochila
print(mochila)

# Acessando dados individuais da tupla:
print('\n')

print(mochila[0]) # mostrará o primeiro elemento do índice.
print(mochila[2]) # mostrará o terceiro elemento do índice.
print(mochila[0:2]) # mostrará o primeiro elemento e o segundo elemnto do índice. Indice 0 e 1
print(mochila[2:]) # Mostrará os elmentos do indice dois até o final. começando do indice 2.
print(mochila[-1]) # motrará o ultimo elemento. no caso, índice 3. Lê ao contrário. De trás para frente.

# Lembrando que tupla não s epode tribuir de forma simples, outros valores.

# Correndo as variáveis dentro de um tupla:
print('\n')

for item in mochila: # OBS: Não usamos RANGE. de forma simples e direta.
    print('Intens dentro da mochila: {}'.format(item))
    # Criado a váriavel "Item" para ser o noem da variavel a percorer
    # citar dentro do print, a variavel no qual se quer que o item seja mostrado. no caso "item"

# usando RANGE:
print('\n')

tam = len(mochila) # criado a variavel que vai contar os iten dentro da variavel mochila
for i in range (0,tam,1): # i = Variavel criada para se percorrer. Inicio, final (varial que dará esse valor), como contar
                          # Parad difinir os lmites do RANGE precisa pegar o tamnho da tuple, no caso com TAM
    print('Intens dentro da mochila: {}'.format(mochila[i])) # dentro do formar tem as variaveis onde existe os elementos alvos.
                                                            # i = informa o indice que sera percorrido, onde o tam sabe o final da contagem.

# Adicionando itens na TUPLA:
print('\n')

upgrade = ('Queijo', 'Canivete')
mochila_atualizada = mochila + upgrade # pega os elemntos da mochila padrão e concatena com o upgrade
print(mochila_atualizada)

# a ordem do upgrade influiencia. no caso o upgrade está concatenado pós mochila. se colocar antes da mochila, ele aprensetará antes.
mochila_atualizada_invertida= upgrade+mochila
print('\n')
print(mochila_atualizada_invertida)


# Desempacotamento de parâmetros em funções:
print('\n')

def soma(*num): # NUM = Nome da variável que virá com parâmetro. o * significa desempacotamento
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

# Objetivo da função denominada SOMA é somar os elementos declarados para ser somado em nos prints abaixo:
# Eles serão enviados ao *NUM,será informado os valores de NUM, no primeiro print na função.
# Será contado e somado os elementos no soma += 1
# e de toda a função, retornará o valor da soma return soma

print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))